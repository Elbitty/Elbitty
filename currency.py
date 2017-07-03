#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests
import NLP
from stringtext import StringProcess
import currdb


def calculate(str_query, to_measure, str_humanize, to_buy = 0, to_sell = 0):

    unit = in_calculate(keyword=str_query)

    to_buy = unit[1] * to_measure
    to_buy = round(to_buy, 2)
    to_sell = unit[0] * to_measure
    to_sell = round(to_sell, 2)

    kor_to_measure = ""
    if to_measure >= 10000:
        kor_to_measure = "(" + StringProcess.korean_number(to_measure) + ") "

    kor_to_buy = ""
    if to_buy >= 10000:
        kor_to_buy = "(" + StringProcess.korean_number(to_buy) + ") "

    kor_to_sell = ""
    if to_sell >= 10000:
        kor_to_sell = "(" + StringProcess.korean_number(to_sell) + ") "

    to_measure = "{:,}".format(float(to_measure)).rstrip('0').rstrip('.')
    to_buy = "{:,.2f}".format(to_buy)
    to_sell = "{:,.2f}".format(to_sell)

    josa_eunnun = [str(""), str("")]
    josa_yigo = [str(""), str("")]
    josa_yeayo = [str(""), str("")]

    for idx in range(2):
        if StringProcess.last_word(StringProcess.right(str_humanize[idx], count=1)) == 0:
            josa_eunnun[idx] = "는"
            josa_yigo[idx] = "고"
        else:
            josa_eunnun[idx] = "은"
            josa_yigo[idx] = "이고"

    response = to_measure + " " + kor_to_measure + str_humanize[0] + josa_eunnun[0] + " \n"
    response = response + "살 때 " + to_buy + " " + kor_to_buy + str_humanize[1] + josa_yigo[1] + ", \n"
    response = response + "팔 때는 " + to_sell + " " + kor_to_sell + str_humanize[1]

    return response


def remove_zero_point(value):
    while True:
        if (StringProcess.right(value) == "0"):
            value = StringProcess.left(value, len(value)-1)
        elif (StringProcess.right(value) == "."):
            value = StringProcess.left(value, len(value)-1)
            break
        else:
            break
    return value


def in_calculate(keyword = "USDKRW"):

    answer = currdb.getcurrndb(keyword)
    if answer is None:
        answer = get_currency(keyword)
        currdb.updatedata(keyword, answer[0], answer[1])
    return answer[0], answer[1]


def get_currency(keyword = "USDKRW"):
    #http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%3D%22USDKRW%22&format=xml&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys

    query = 'select * from yahoo.finance.xchange where pair="' + keyword + '"'
    params = {
        "q" : query,
        "format" : "json",
        "diagnostics" : "true",
        "env" : "store://datatables.org/alltableswithkeys"
        }

    data = requests.get("http://query.yahooapis.com/v1/public/yql", params=params)
    json_content = json.loads(data.content)

    
    bid = float(json_content['query']['results']['rate']['Bid'])
    ask = float(json_content['query']['results']['rate']['Ask'])

    print(json_content['query']['results']['rate'])
    return(bid, ask)


if __name__ == "__main__":
    print()
