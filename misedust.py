#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests
from stringtext import StringProcess

def calculate(tags):

    addr = tags[0]
    latt = tags[1]
    longt = tags[2]

    calc = calculate_in_module(latt, longt)

    tmp_value = float(calc[1])

    if (tmp_value % 1) == 0:
        value = "{:,.0f}".format(tmp_value)
    else:
        value = "{}".format(tmp_value)



    if (StringProcess.right(value) == "3") or (StringProcess.right(value) == "6"):
        josa = "으로"
    else:
        josa = "로"

    status = addr + "의 미세먼지(pm10) 수치는 " + value + josa + ", " + calc[0] + " 등급" #이에요.

    return status


def calculate_in_module(latt, lont):

    lat = latt
    lon = lont

    params = {'version' : '1', 'lat' : lat, 'lon' : lon}
    headers = {'appKey' : '6bcdca7c-f848-3935-8eae-2fe837afaafb'}

    data = requests.get("http://apis.skplanetx.com/weather/dust", params=params, headers=headers)

    jsons = json.loads(data.content)
    print(jsons)
    try:
        grade = jsons["weather"]["dust"][0]["pm10"]["grade"]
        value = jsons["weather"]["dust"][0]["pm10"]["value"]
        return grade, value
    except:
        return False


if __name__ == '__main__':
    print(calculate("서울특별시"))
