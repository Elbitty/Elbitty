#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from pyowm import OWM
from locnlp import LocNLP
from stringtext import StringProcess

def calculate(tags):

    WEATHER_FILE = 'weather.Status.txt'

    API_KEY = '.'

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

    addr = tags[0]
    latt = tags[1]
    longt = tags[2]

    owm = OWM(API_KEY)

    obs = owm.weather_at_coords(latt, longt)
    obs_weather = obs.get_weather()
    w_status = obs_weather.get_status()

    w_celcius = float(obs_weather.get_temperature(unit='celsius')['temp'])

    if (w_celcius % 1) == 0:
        w_celcius = "{:,.0f}".format(w_celcius)
    else:
        w_celcius = "{}".format(w_celcius)# {:,.2f}

    weatherstatus = open(os.path.join(THIS_FOLDER, WEATHER_FILE), 'r')
    w_result = parse_as_dic(weatherstatus)
    print(w_result)
    print(w_status)
    w_status = dic_instr(w_result, w_status)

    w_status = addr + w_status + "기온은 " + w_celcius + "℃" #예요.
    return w_status

def parse_as_dic(input_string):
    splitted = [(line.strip("\n")).split('::') for line in input_string.readlines()]
    return dict(splitted)
    #return dict([[s[0], s[1].strip("\n")] for s in [ln.split('::') for ln in strinput.readlines()]])

def dic_instr(dic, fullstr):
    for key_word in dic.keys():
        if key_word in fullstr:
            final = dic[key_word]
            break
    return final


if __name__ == '__main__':

    print(calculate(["동대문구", "어떠"]))
