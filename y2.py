#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import tweepy
import response
import analysis
import apilimit

print("작동 시작.")

SPACE_CHAR = str(" ")
NL_CHAR = "\n"
AT_CHAR = "@"

CK = ""
CS = ""
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
AT = ""
AS = ""

# Twitter 오브젝트의 생성자
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

ADMIN_ID = '_circonor'

USER_LIMIT_TIME = 1


print("screen_name 가져오기." + NL_CHAR)
NAME_OF_BOT = api.me().screen_name #pylint에서 오류로 표시되나 오류 아니며 정상작동됨.

NAME_OF_BOT = str(NAME_OF_BOT)
print(NAME_OF_BOT)

print("FRIEND_LIST 가져오기.")
FRIEND_LIST = api.friends_ids(NAME_OF_BOT)


class Listener(tweepy.StreamListener):

    def __init__(self, api=None):
        self.api = api or tweepy.API()
        self.__tweet_count = 0
        self.__calculated = 0

    def on_status(self, status):
        status.created_at += datetime.timedelta(hours=9)
        # UTC +9
        if (str(status.in_reply_to_screen_name) == NAME_OF_BOT) and (status.user.id in FRIEND_LIST):
            #해당 Mention이 BOT에게 Reply 되었는가, 또한, 해당 Mention이 FRIEND_LIST의 elements중 하나에게서 왔는가.

            to_reply = str(status.user.screen_name)

            most_recent_tweet = response.run(api, to_reply, NAME_OF_BOT)#Reply 1개 받아오기.
            print(most_recent_tweet)

            if to_reply == ADMIN_ID:
                is_admin = True
            else:
                is_admin = False
                check_is_userlimit = apilimit.isuserlimit(status.user.id, USER_LIMIT_TIME)

            if not is_admin and check_is_userlimit is not False:
                str_response = check_is_userlimit + "에 AI를 이용하셨습니다. " +\
                                str(USER_LIMIT_TIME) + " 분만 기다려 주세요."
            else:
                tweets = most_recent_tweet[0]#0번째 Element는 자연어 분석된 tweet 본문 내의 태그 List.
                #1번째 Element는 String 형의 status_user_id이다. screen_name이 아님에 유의.
                tweets = tweets.replace('@' + NAME_OF_BOT, '')
                tweets = tweets.replace(NAME_OF_BOT, '')
                responsed = analysis.calculate(tweets, is_admin, self.__calculated)
                self.__calculated = responsed[1]
                str_response = responsed[0] #반환할 트윗의 내용

            self.__tweet_count += 1

            tweet_count_str = str(self.__tweet_count)
            length_of_tweet_count_str = len(tweet_count_str) + len("\n\n<>")

            str_response = AT_CHAR + to_reply +  SPACE_CHAR + str_response

            if len(str_response) > (140-length_of_tweet_count_str):
                str_response = str_response[0:(139-length_of_tweet_count_str)] + "…"

            str_response = str_response + "\n\n<" + tweet_count_str + ">"


            api.update_status(status=str_response, \
                in_reply_to_status_id=most_recent_tweet[1])

            print(str_response + NL_CHAR)

        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

# Twitter 오브젝트의 생성자
#auth = tweepy.OAuthHandler(CK, CS)
#auth.set_access_token(AT, AS)

now = datetime.datetime.now()
now_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

api.update_status(status="서버 시각 " + now_datetime + ".\nLBT 서버가 시작되었습니다.")
api.update_status(status=AT_CHAR + ADMIN_ID + SPACE_CHAR + now_datetime + \
"\nLBT가 켜 졌어요, 주인님. \n오늘도 잘 부탁드려요.")
print("최종 과정. 이 단계가 완료되면 정상적으로 사용할 수 있습니다." + NL_CHAR)

listener = Listener()
stream = tweepy.Stream(auth, listener)

is_excepted = True

while is_excepted:
    try:
        stream.userstream()
        is_excepted = False
    except Exception as exc:
        print("\n예외 : " + str(exc))
        api.update_status(status=AT_CHAR + ADMIN_ID + SPACE_CHAR + now_datetime + \
"\n트위터 서버와 통신 문제로 예외가 발생했어요. : " + str(exc))
        is_excepted = True
