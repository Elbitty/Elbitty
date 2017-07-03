#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import datetime
import NLP
import apilimit
import locdb
from stringtext import StringProcess
import currnlp
import currdb

def calculate(text, is_admin=False):

    j_tags = NLP.calculate(text)
    tags = NLP.calculate_except_josa(text) #조사 제외 전체
    n_tags = NLP.calculate_only_nouns(text) #명사 태그

    curr_tags_with_pos =  NLP.calculate_currency(text)
    curr_tags = [curr_tags_with_pos[x][0] for x in range(len(curr_tags_with_pos ))]
    print(tags)

    EMPTY_TEXT = str('')

    if isin(["모듈", "기능", "작동"], tags):
        if "날씨" in tags:
            str_response = to_admin_or_user("날씨 모듈은 작동", is_admin, "하고 있어요.", "하고 있습니다.")
        else:
            str_response = to_admin_or_user("지금은 <자연어 처리>, <자동 응답>, [상품 자연어 처리], [Shopping], [지역 자연어 처리], [Location], [통화 자연어 처리], [Currency], [키워드 자연어 처리], [Encyclopedia], [미세 먼지], [날씨] 모듈이 작동",
                                            is_admin, 
                                            "하고 있어요.", 
                                            "하고 있습니다.")






    elif isin(["미세먼지", "미세", "먼지", "농도", "공기", "대기", "대다"], tags):
        import misedust
        n_tags = remove_if_exsits(n_tags, ["오늘", "지금", "현재"])
        n_tags = cut_to_item(["미세먼지", "미세", "먼지"], n_tags)
        print(n_tags)
        n_tags = set_default(["미세먼지", "미세", "먼지"], n_tags)
        print(n_tags)
        location = locdb.getlocationdb(n_tags)

        tmp_find = apilimit.isapilimit("misedust_pm10", location[0])
        if tmp_find != None:
            str_response = tmp_find[0]
            upd_time = now_time(tmp_find[1])
            print("anly_1")
        else:
            str_response = misedust.calculate(location)
            apilimit.apilimitupdate("misedust_pm10", location[0], str_response)
            print("anly_2")
            upd_time = now_time(now_float())

        str_response = to_admin_or_user(str_response, is_admin, "이에요.", "입니다.")
        str_response = str_response + "\n(" + upd_time + "에 갱신"
        str_response = to_admin_or_user(str_response, is_admin, "되었어요.", "됨.")
        str_response = str_response + ")"






    elif isin(["날씨", "오늘", "지금", "현재", "기온", "온도", "맑다", "흐리다", "비다"], tags):
        import weather
        n_tags = remove_if_exsits(n_tags, ["오늘", "지금", "현재"])
        n_tags = cut_to_item(["날씨", "기온", "온도"], n_tags)
        print(n_tags)
        n_tags = set_default(["날씨", "기온", "온도"], n_tags)
        print(n_tags)
        location = locdb.getlocationdb(n_tags)

        tmp_find = apilimit.isapilimit("weather", location[0])
        if tmp_find != None:
            str_response = tmp_find[0]
            upd_time = now_time(tmp_find[1])
            print("anly_1")
        else:
            str_response = weather.calculate(location)
            apilimit.apilimitupdate("weather", location[0], str_response)
            print("anly_2")
            upd_time = now_time(now_float())

        str_response = to_admin_or_user(str_response, is_admin, "예요.", "입니다.")
        str_response = str_response + "\n(" + upd_time + "에 갱신"
        str_response = to_admin_or_user(str_response, is_admin, "되었어요.", "됨.")
        str_response = str_response + ")"






    elif isin(["환율", "KRW", "USD", "JPY", "EUR", "CNY", "RUB", "GBP", "CAD"], curr_tags):
        import currency
        curr_tags = remove_if_exsits(curr_tags, ["오늘", "지금", "현재"])
        curr_tags = cut_to_item(["환율"], curr_tags)

        curr_tag =  currnlp.calculate(curr_tags_with_pos) #curr_tag의 구조는 예. ("USDKRW", 50000, ("원","달러"))
        tmp_find = currdb.getcurrndb(curr_tag[0])#tmp_find 의 구조는 None  or (bid, ask, last_requested_time)

        if tmp_find != None:
            str_response = currency.calculate(curr_tag[0], curr_tag[1], curr_tag[2],
                                              tmp_find[0], tmp_find[1])
            upd_time = now_time(tmp_find[2])
            print("anly_1")
        else:
            tmp_find = currency.get_currency(curr_tag[0])
            currdb.updatedata(curr_tag[0], tmp_find[0], tmp_find[1])
            str_response = currency.calculate(curr_tag[0], curr_tag[1], curr_tag[2],
                                              tmp_find[0], tmp_find[1])
            print("anly_2")
            upd_time = now_time(now_float())

        if StringProcess.last_word(StringProcess.right(str_response, count=1)) == 0:
            josa_yeayo = "예요."
        else:
            josa_yeayo = "이에요."

        str_response = to_admin_or_user(str_response, is_admin, josa_yeayo, "입니다.")
        str_response = str_response + "\n(" + upd_time + "에 갱신"
        str_response = to_admin_or_user(str_response, is_admin, "되었어요.", "됨.")
        str_response = str_response + ")"






    elif isin(["가격", "제품", "상품", "얼마"], tags):
        import shopanalysis
        n_tags = remove_if_exsits(n_tags, ["오늘", "지금", "현재"])
        n_tags = cut_to_item(["가격", "제품", "상품", "얼마", "최저", "최고"], n_tags)

        r_q = NLP.calculate_no_norm(text)
        tmpr = str("")
        for val in r_q:
            if (val[1] == "Josa") or (val[1] == "Eomi") or (val[1] == "Alpha") or (val[1] == "Number"):
                tmpr = tmpr + val[0]
            else:
                tmpr = tmpr + " " + val[0]
        n_text = tmpr

        tmp_find = apilimit.isapilimit("shopping", n_text)
        if tmp_find != None:
            str_response = tmp_find[0]
            upd_time = now_time(tmp_find[1])
            print("anly_1")
        else:
            str_response = shopanalysis.calculate(n_tags)
            apilimit.apilimitupdate("shopping", n_text, str_response)
            print("anly_2")
            upd_time = now_time(now_float())

        if str_response == "NA":
            str_response = to_admin_or_user("그", is_admin,
                                            " 제품은 확인 할 수 없었어요.", "런 제품명은 존재하지 않습니다.")
        else:
            str_response = to_admin_or_user(str_response, is_admin, "이에요.", "입니다.")
            str_response = str_response + "\n(" + upd_time + "에 갱신"
            str_response = to_admin_or_user(str_response, is_admin, "되었어요.", "됨.")
            str_response = str_response + ")"






    elif isin(["뭐", "무엇", "어떻다", "알다", "누구", "대해", "대하다", "관", "관해", "관련", "정보", "란", "이란"], j_tags):
        import encyclonlp
        import encyclopedia

        curr_tag =  encyclonlp.calculate(text)#
        tmp_find = apilimit.isapilimit("encyclopedia", curr_tag, 43800)

        if tmp_find != None:
            str_response = tmp_find[0]
            upd_time = now_time(tmp_find[1])
            print("anly_1")
        else:
            str_response = encyclopedia.calculate(curr_tag)
            #str_response = str_response
            apilimit.apilimitupdate("encyclopedia", curr_tag, str_response.replace("'", "''"))
            print("anly_2")
            upd_time = now_time(now_float())

        if str_response == "NA":
            str_response = to_admin_or_user(curr_tag, is_admin,
                                            "에 대한 정보를 찾을 수 없었어요.", "에 대한 정보가 존재하지 않습니다.")
        else:

            if (StringProcess.right(str_response, count=1) == "…"):
                pass
            else:
                to_find_josa = re.sub('\W+', '', str_response)

                if (StringProcess.right(to_find_josa, count=1) == "했") or \
                (StringProcess.right(to_find_josa, count=1) == "였") or \
                (StringProcess.right(to_find_josa, count=1) == "있") or \
                (StringProcess.right(to_find_josa, count=1) == "없"):
                    str_response = to_admin_or_user(str_response, is_admin, "어요.", "습니다.")
                elif (StringProcess.right(to_find_josa, count=1) == "함") or (StringProcess.right(to_find_josa, count=1) == "한"):
                    str_response = StringProcess.left(str_response, len(str_response)-1)
                    str_response = to_admin_or_user(str_response, is_admin, "해요.", "합니다.")
                elif (StringProcess.right(to_find_josa, count=1) == "된"):
                    str_response = StringProcess.left(str_response, len(str_response)-1)
                    str_response = to_admin_or_user(str_response, is_admin, "되어요.", "됩니다.")
                elif (StringProcess.right(to_find_josa, count=1) == "됨"):
                    str_response = StringProcess.left(str_response, len(str_response)-1)
                    str_response = to_admin_or_user(str_response, is_admin, "되어요.", "됩니다.")
                else:
                    if StringProcess.last_word(StringProcess.right(to_find_josa, count=1)) == 0:
                        josa_yeayo = "예요."
                    else:
                        josa_yeayo = "이에요."
                    str_response = to_admin_or_user(str_response, is_admin, josa_yeayo, "입니다.")

            #str_response = str_response + "\n(" + upd_time + "에 갱신"
            #str_response = to_admin_or_user(str_response, is_admin, "되었어요.", "됨.")
            #str_response = str_response + ")"






    else:
        tag = " ".join(str(val) for val in tags)
        print(tag)
        arr_from = ["테스트", "안녕", "뭐 하다",
                    "엘비티", "잘하다"]

        admin_arr_to = ["저는 잘 작동하고 있어요, 주인님.", "안녕하세요, 주인님.", "저는 잘 작동하고 있어요, 주인님.",
                        "부르셨나요, 주인님?", "고맙습니다, 주인님."]

        user_arr_to = ["이상 없습니다.", "안녕하십니까.", "작동중 입니다.", "부르셨습니까?", "알겠습니다."]

        str_response = to_admin_or_user(EMPTY_TEXT, is_admin,
                                        "죄송해요 주인님, 잘 알아듣지 못했어요.", "잘 알아듣지 못했습니다.")
        for idx, tmp_from in enumerate(arr_from):
            if tmp_from in tag:
                if is_admin:
                    str_response = admin_arr_to[idx]
                else:
                    str_response = user_arr_to[idx]
                break

    return str_response

        #if "몇 시" in StringAll:





def remove_if_exsits(list_to_remove, items):
    for val in items:
        if val in list_to_remove:
            list_to_remove.remove(val)
    return list_to_remove

def isin(keywords, text_or_tags):
    indicator = False
    for val in keywords:
        if val in text_or_tags:
            indicator = True
            break
    return indicator

def cut_to_item(keywords, tags):
    if len(tags) > 1:
        for val in keywords:
            if val in tags:
                tags = tags[0:tags.index(val)]
    else:
        pass
    return tags

def set_default(keywords, listx, default_value = "서울특별시"):
    for val in keywords:
        if listx[0] == val:
            listx.insert(0, default_value)
            break
    return listx

def to_admin_or_user(main_text, is_admin, to_admin, to_user):
    if is_admin:
        return main_text + to_admin
    else:
        return main_text + to_user

def request_delayed(last_request_time, delay):
    if isinstance(last_request_time, tuple):
        for val in last_request_time:
            if (now_float() - int(val)) > (delay*60):
                return True
            else:
                return False
    else:
        if (now_float() - int(last_request_time)) > (delay*60):
            return True
        else:
            return False

def now_float():
    return int(datetime.datetime.now().timestamp())

def now_time(unix_time):
    return datetime.datetime.fromtimestamp(
        int(unix_time)
    ).strftime('%Y-%m-%d %H:%M:%S')



if __name__ == "__main__":
    print(calculate("a6500 가격"))
