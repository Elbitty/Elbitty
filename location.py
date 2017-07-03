#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests


def calculate(area):

    location = area

    params = {"sensor" : "false", "language" : "ko", "address" : location}

    data = requests.get("http://maps.googleapis.com/maps/api/geocode/json", params=params)
    json_content = json.loads(data.content)

    try:
        address = json_content["results"][0]["formatted_address"]
        latitude = json_content["results"][0]["geometry"]["location"]["lat"]
        longitude = json_content["results"][0]["geometry"]["location"]["lng"]
        return address, latitude, longitude

    except IndexError as exp:
        print(json_content["status"])
        print(exp)
        return False


if __name__ == '__main__':
    print(calculate("부산 해운대 시공조아"))
