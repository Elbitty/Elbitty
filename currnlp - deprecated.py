#!/usr/bin/env python
# -*- coding:utf-8 -*-

import NLP


def calculate(tags):
    tmp_str = " ".join(str(val) for val in tags)
    tmp_tags = NLP.calculate_also_pos(tmp_str)
    print(tmp_tags)
    lst_query = ["USD", "KRW"]#기본 원달러 환율로 초기화
    str_humanize = ["달러", "원"]#기본 원달러 환율로 초기화

    indicator = 0
    cursor = 0
    value_of_currency = 1
    multiplier = 1

    for idx, val in enumerate(tmp_tags):

        if val[1] == "Number":
            if (idx - cursor) < 2:
                value_of_currency = float(val[0])

        if (idx - cursor) < 3:
            if val[0] == "십":
                multiplier = 10
                cursor = idx
            if val[0] == "백":
                multiplier = 100
                cursor = idx
            if val[0] == "천":
                multiplier = 1000
                cursor = idx
            if val[0] == "만":
                multiplier = 10000
                cursor = idx
            if val[0] == "십만":
                multiplier = 100000
                cursor = idx
            if val[0] == "백만":
                multiplier = 1000000
                cursor = idx
            if val[0] == "천만":
                multiplier = 10000000
                cursor = idx
            if val[0] == "억":
                multiplier = 100000000
                cursor = idx
            if val[0] == "십억":
                multiplier = 1000000000
                cursor = idx

        if (val[0] == "원") or (val[0] == "원화") or (val[0] == "KRW"):
            str_humanize[indicator] = "원"
            lst_query[indicator] = "KRW"
            cursor = idx
            indicator += 1
        elif val[0] == "십원":
            str_humanize[indicator] = "원"
            lst_query[indicator] = "KRW"
            cursor = idx
            multiplier = 10
            indicator += 1
        elif val[0] == "백원":
            str_humanize[indicator] = "원"
            lst_query[indicator] = "KRW"
            cursor = idx
            multiplier = 100
            indicator += 1
        elif val[0] == "천원":
            str_humanize[indicator] = "원"
            lst_query[indicator] = "KRW"
            cursor = idx
            multiplier = 1000
            indicator += 1
        elif val[0] == "만원":
            str_humanize[indicator] = "원"
            lst_query[indicator] = "KRW"
            cursor = idx
            multiplier = 10000
            indicator += 1
        elif val[0] == "십만원":
            str_humanize[indicator] = "원"
            lst_query[indicator] = "KRW"
            cursor = idx
            multiplier = 100000
            indicator += 1
        elif val[0] == "백만원":
            str_humanize[indicator] = "원"
            lst_query[indicator] = "KRW"
            cursor = idx
            multiplier = 1000000
            indicator += 1
        elif val[0] == "천만원":
            str_humanize[indicator] = "원"
            lst_query[indicator] = "KRW"
            cursor = idx
            multiplier = 10000000
            indicator += 1
        elif val[0] == "억원":
            str_humanize[indicator] = "원"
            lst_query[indicator] = "KRW"
            cursor = idx
            multiplier = 100000000
            indicator += 1

        elif (val[0] == "달러") or (val[0] == "달러화"):
            str_humanize[indicator] = "달러"
            lst_query[indicator] = "USD"
            cursor = idx
            indicator += 1

        elif (val[0] == "엔") or (val[0] == "엔화") or (val[0] == "JPY"):
            str_humanize[indicator] = "엔"
            lst_query[indicator] = "JPY"
            cursor = idx
            indicator += 1
        elif val[0] == "십엔":
            str_humanize[indicator] = "엔"
            lst_query[indicator] = "JPY"
            cursor = idx
            multiplier = 10
            indicator += 1
        elif val[0] == "백엔":
            str_humanize[indicator] = "엔"
            lst_query[indicator] = "JPY"
            cursor = idx
            multiplier = 100
            indicator += 1
        elif val[0] == "천엔":
            str_humanize[indicator] = "엔"
            lst_query[indicator] = "JPY"
            cursor = idx
            multiplier = 1000
            indicator += 1
        elif val[0] == "만엔":
            str_humanize[indicator] = "엔"
            lst_query[indicator] = "JPY"
            cursor = idx
            multiplier = 10000
            indicator += 1
        elif val[0] == "십만엔":
            str_humanize[indicator] = "엔"
            lst_query[indicator] = "JPY"
            cursor = idx
            multiplier = 100000
            indicator += 1
        elif val[0] == "백만엔":
            str_humanize[indicator] = "엔"
            lst_query[indicator] = "JPY"
            cursor = idx
            multiplier = 1000000
            indicator += 1
        elif val[0] == "천만엔":
            str_humanize[indicator] = "엔"
            lst_query[indicator] = "JPY"
            cursor = idx
            multiplier = 10000000
            indicator += 1

        elif (val[0] == "유로") or (val[0] == "유로화") or (val[0] == "EUR"):
            str_humanize[indicator] = "유로"
            lst_query[indicator] = "EUR"
            cursor = idx
            indicator += 1
        elif (val[0] == "위안") or (val[0] == "위안화") or (val[0] == "CNY"):
            str_humanize[indicator] = "위안"
            lst_query[indicator] = "CNY"
            cursor = idx
            indicator += 1

    to_measure = int(value_of_currency * multiplier)

    if (to_measure == 1) and (not indicator <= 1):
        str_humanize.reverse()
        str_query = lst_query[1] + lst_query[0]
    else:
        str_query = lst_query[0] + lst_query[1]

    return str_query, to_measure, str_humanize


if __name__ == "__main__":
    print(calculate(['50', '만엔', '얼마']))
