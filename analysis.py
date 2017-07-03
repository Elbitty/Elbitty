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

#===================================================================================================

is_info = ["기능", "모듈", "작동"]
is_currency = ["환율", "원", "달러", "엔", "유로", "위안", "루블", "파운드"]
is_encyclopedia = ["무엇", "뭐", "누구", "대해", "대하다", "관", "관해", "관련", "정보", "란", "이란"]
is_misedust = ["미세먼지", "미세", "먼지", "농도", "공기", "대기", "대다"]
is_weather = ["날씨", "오늘", "지금", "현재", "기온", "온도", "맑다", "흐리다", "비다"]
is_shopping = ["가격", "제품", "상품", "얼마"]
is_remind = ["깨우다"]

def aa():
    print(is_info)

#===================================================================================================
def calculate(text, is_admin=False, calculated=0):
    tags = NLP.calculate(text)
    tmpis = []
    tmpis.extend(is_info)
    tmpis.extend(is_encyclopedia)
    tmpis.extend(is_misedust)
    tmpis.extend(is_weather)
    tmpis.extend(is_shopping)
    tmpis.extend(is_remind)

    if isin(tmpis, tags) or isin(is_currency, text):
        pass
    else:
        if calculated == 1:
            text = text + " " + is_info[0]
        elif calculated == 2:
            text = text + " " + is_currency[0]
        elif calculated == 3:
            text = text + " " + is_encyclopedia[0]
        elif calculated == 4:
            text = text + " " + is_misedust[0]
        elif calculated == 5:
            text = text + " " + is_weather[0]
        elif calculated == 6:
            text = text + " " + is_shopping[0]
        elif calculated == 7:
            text = text + " " + is_remind[0]
        else:
            pass

    return_value = calculate_in_module(text, is_admin, calculated)
    return return_value

#------------------------------------------------------------------------
def calculate_in_module(text, is_admin=False, calculated=0):
    tags = NLP.calculate(text)

    if isin(is_info, tags):
        str_response = info_do(text, is_admin)
        calculated = 1

    elif isin(is_currency, text):
        str_response = currency_do(text, is_admin)
        calculated = 2

    elif isin(is_encyclopedia, tags):
        str_response = encyclopedia_do(text, is_admin)
        calculated = 3

    elif isin(is_misedust, tags):
        str_response = misedust_do(text, is_admin)
        calculated = 4

    elif isin(is_weather, tags):
        str_response = weather_do(text, is_admin)
        calculated = 5

    elif isin(is_shopping, tags):
        str_response = shopping_do(text, is_admin)
        calculated = 6

    elif isin(is_remind, tags):
        str_response = remind_do(text, is_admin)
        calculated = 6

    else:
        EMPTY_TEXT = str('')
        tag = " ".join(str(val) for val in tags)
        print(tag)
        arr_from = ["테스트", "안녕", "뭐 하다",
                    "엘비티", "잘하다"]
        admin_arr_to = ["저는 잘 작동하고 있어요, 주인님.", "안녕하세요, 주인님.", "저는 잘 작동하고 있어요, 주인님.",
                        "부르셨나요, 주인님?", "고맙습니다, 주인님."]
        user_arr_to = ["이상 없어요.", "안녕하세요?", "작동중이에요.", "부르셨나요?", "알겠어요."]
        str_response = to_admin_or_user(EMPTY_TEXT, is_admin,
                                        "죄송해요 주인님, 잘 알아듣지 못했어요.", "잘 알아듣지 못했어요.")
        for idx, tmp_from in enumerate(arr_from):
            if tmp_from in tag:
                if is_admin:
                    str_response = admin_arr_to[idx]
                else:
                    str_response = user_arr_to[idx]
                break

    return str_response, calculated

#===================================================================================================

def info_do(text, is_admin):
    if "날씨" in text:
        str_response = to_admin_or_user("날씨 모듈은 작동", is_admin, "하고 있어요.", "하고 있습니다.")
    else:
        str_response = to_admin_or_user("지금은 <자연어 처리>, <자동 응답>, " +\
         "[상품 자연어 처리], [Shopping], [지역 자연어 처리], [Location], [통화 자연어 처리], " +\
          "[Currency], [키워드 자연어 처리], [Encyclopedia], [미세 먼지], [날씨] 모듈이 작동",
                                        is_admin,
                                        "하고 있어요.",
                                        "하고 있습니다.")
    return str_response

#===================================================================================================

def remind_do(text, isadmin):
    return "아직 이 기능은 지원하지 않아요."

#===================================================================================================

def shopping_do(text, is_admin):
    import shopanalysis
    n_tags = NLP.calculate_only_nouns(text) #명사 태그
    n_tags = remove_if_exsits(n_tags, ["오늘", "지금", "현재"])
    n_tags = cut_to_item(["가격", "제품", "상품", "얼마", "최저", "최고"], n_tags)

    r_q = NLP.calculate_no_norm(text)
    tmpr = str('')
    for val in r_q:
        if (val[1] == "Josa") or (val[1] == "Eomi") or (val[1] == "Alpha") or (val[1] == "Number"):
            tmpr = tmpr + val[0]
        else:
            tmpr = tmpr + " " + val[0]
    n_text = tmpr

    tmp_find = apilimit.isapilimit("shopping", n_text, 360)
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
        str_response = to_admin_or_user(str_response, is_admin, "이에요.", "이군요.") + "\n(" +\
         upd_time + to_admin_or_user("에 갱신", is_admin, "되었어요.", "되었네요.") + ")"
    return str_response

#===================================================================================================

def encyclopedia_do(text, is_admin):
    import encyclonlp
    import encyclopedia

    curr_tag = encyclonlp.calculate(text)#
    tmp_find = apilimit.isapilimit("encyclopedia", curr_tag, 131400)

    if tmp_find != None:
        str_response = tmp_find[0]
        #upd_time = now_time(tmp_find[1])
        print("anly_1")
    else:
        str_response = encyclopedia.calculate(curr_tag)
        apilimit.apilimitupdate("encyclopedia", curr_tag, str_response)
        print("anly_2")
        #upd_time = now_time(now_float())

    if str_response == "NA":
        str_response = to_admin_or_user(curr_tag, is_admin,
                                        "에 대한 정보를 찾을 수 없었어요.", "에 대한 정보가 존재하지 않아요.")
    else:
        if StringProcess.right(str_response, count=1) == "…":
            pass
        else:
            to_find_josa = re.sub(r'\W+', '', str_response)

            if (StringProcess.right(to_find_josa, count=1) == "했") or \
            (StringProcess.right(to_find_josa, count=1) == "였") or \
            (StringProcess.right(to_find_josa, count=1) == "있") or \
            (StringProcess.right(to_find_josa, count=1) == "없"):

                str_response = to_admin_or_user(str_response, is_admin, "어요.", "군요.")

            elif (StringProcess.right(to_find_josa, count=1) == "함") or\
             (StringProcess.right(to_find_josa, count=1) == "한"):

                str_response = StringProcess.left(str_response, len(str_response)-1)
                str_response = to_admin_or_user(str_response, is_admin, "해요.", "하네요.")

            elif StringProcess.right(to_find_josa, count=1) == "된":
                str_response = StringProcess.left(str_response, len(str_response)-1)
                str_response = to_admin_or_user(str_response, is_admin, "되어요.", "되네요.")

            elif StringProcess.right(to_find_josa, count=1) == "됨":
                str_response = StringProcess.left(str_response, len(str_response)-1)
                str_response = to_admin_or_user(str_response, is_admin, "되어요.", "되네요.")

            else:
                if StringProcess.last_word(StringProcess.right(to_find_josa, count=1)) == 0:
                    josa_yeayo = "예요."
                else:
                    josa_yeayo = "이에요."
                str_response = to_admin_or_user(str_response, is_admin, josa_yeayo, "이군요.")
    return str_response

#===================================================================================================

def misedust_do(text, is_admin):
    import misedust
    n_tags = NLP.calculate_only_nouns(text) #명사 태그
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

    str_response = to_admin_or_user(str_response, is_admin, "이에요.", "이군요.") + "\n(" +\
     upd_time + to_admin_or_user("에 갱신", is_admin, "되었어요.", "되었네요.") + ")"
    return str_response

#===================================================================================================

def weather_do(text, is_admin):
    import weather
    n_tags = NLP.calculate_only_nouns(text) #명사 태그
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

    str_response = to_admin_or_user(str_response, is_admin, "예요.", "군요.") + "\n(" +\
     upd_time + to_admin_or_user("에 갱신", is_admin, "되었어요.", "되었네요.") + ")"
    return str_response

#===================================================================================================

def currency_do(text, is_admin):
    import currency
    curr_tags_with_pos = NLP.calculate_currency(text)
    curr_tags = [curr_tags_with_pos[x][0] for x in range(len(curr_tags_with_pos))]

    curr_tags = remove_if_exsits(curr_tags, ["오늘", "지금", "현재"])
    curr_tags = cut_to_item(["환율"], curr_tags)

    curr_tag = currnlp.calculate(curr_tags_with_pos)#curr_tag의 구조는 예. ("USDKRW", 50000, ("원","달러"))
    tmp_find = currdb.getcurrndb(curr_tag[0])#tmp_find 의 구조는 None or (bid, ask, last_requested_time)

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
        josa_yeayo_admin = "예요."
        josa_yeayo_user = "군요."
    else:
        josa_yeayo_admin = "이에요."
        josa_yeayo_user = "이군요."

    str_response = to_admin_or_user(str_response, is_admin, josa_yeayo_admin, josa_yeayo_user) + "\n(" +\
     upd_time + to_admin_or_user("에 갱신", is_admin, "되었어요.", "되었네요.") + ")"
    return str_response

#===================================================================================================

def remove_if_exsits(list_to_remove, items):
    for val in items:
        if val in list_to_remove:
            list_to_remove.remove(val)
    return list_to_remove

#------------------------------------------------------------------------
def isin(keywords, text_or_tags):
    indicator = False
    for val in keywords:
        if val in text_or_tags:
            indicator = True
            break
    return indicator

#------------------------------------------------------------------------
def cut_to_item(keywords, tags):
    if len(tags) > 1:
        for val in keywords:
            if val in tags:
                tags = tags[0:tags.index(val)]
    else:
        pass
    return tags

#------------------------------------------------------------------------
def set_default(keywords, listx, default_value="서울특별시"):
    if listx == []:
        listx.append(default_value)
        return listx

    for val in keywords:
        if listx[0] == val:
            listx[0] = default_value#listx.insert(0, default_value)
            break
    return listx

#------------------------------------------------------------------------
def to_admin_or_user(main_text, is_admin, to_admin, to_user):
    if is_admin:
        return main_text + to_admin
    else:
        return main_text + to_user

#------------------------------------------------------------------------
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

#------------------------------------------------------------------------
def now_float():
    return int(datetime.datetime.now().timestamp())

#------------------------------------------------------------------------
def now_time(unix_time):
    return datetime.datetime.fromtimestamp(
        int(unix_time)
    ).strftime('%Y-%m-%d %H:%M:%S')

#===================================================================================================

if __name__ == "__main__":
    print(calculate("사당 모펀 근처 날씨", False, 4))
