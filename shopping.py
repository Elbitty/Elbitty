#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests


def calculate(keyword):

    query = keyword

    api_key = ""

    params = {"apikey" : api_key, "q" : query, "result" : "20", "sort" : "pop", "output" : "json"}

    data = requests.get("https://apis.daum.net/shopping/search", params=params)
    json_content = json.loads(data.content)

    try:
        if json_content['channel']['totalCount'] > 0:
            maker = json_content['channel']['item'][0]['maker']
            title = json_content['channel']['item'][0]['title']
            price_min = json_content['channel']['item'][0]['price_min']
            price_max = json_content['channel']['item'][0]['price_max']
            return maker, title, price_min, price_max
        else:
            return None

    except IndexError as exp:
        print(json_content["status"])
        print(exp)
        return False


if __name__ == '__main__':
    print(calculate("플레이스테이션 4"))
