#!/usr/bin/env python
# -*- coding:utf-8 -*-

from stringtext import StringProcess
import htmltext

def run(api, to_reply, from_reply):#toReply는 사용자, fromReply는 AI 봇을 받는 String 인수이다.

    if StringProcess.left(from_reply) != '@':
        from_reply = '@' + from_reply

    print(from_reply)

    tweets = api.user_timeline(screen_name=to_reply, count=1)

    for idx, tweet in enumerate(tweets):
        modyfied_tweet = htmltext.unescape(tweet.text)
        if idx >= 1:
            break

    print(modyfied_tweet)

    if from_reply.lower() in modyfied_tweet.lower():
    #대소문자가 구분될 시 이번 분기의 조건식이 False로 인식될 수 있으므로, 비교자 및 비교대상자 lowercase로 변환.
        return modyfied_tweet, tweet.id#, tweet.user.location
    else:
        return False




if __name__ == "__main__":
    pass
