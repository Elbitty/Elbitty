#!/usr/bin/env python
# -*- coding:utf-8 -*-

def calculate(tags):
    print(tags)
    tmp_tags = tags
    print(tmp_tags)
    lst_query = ["USD", "KRW"]#기본 원달러 환율로 초기화
    str_humanize = ["달러", "원"]#기본 원달러 환율로 초기화

    cursor = [False, False]

    indicator = 0
    #cursor = 0
    number_cursor = 0
    value_of_currency = 1
    multiplier = 1

    for idx, val in enumerate(tmp_tags):

        if val[1] == "Number":
            if cursor[0] is False:
                value_of_currency = float(val[0])
                number_cursor = idx

        elif val[1] == "Alpha":
            if (val[0] == "KRW"):
                str_humanize[indicator] = "원"
                lst_query[indicator] = "KRW"
                #cursor = idx
                cursor[0] = True
                indicator += 1

            elif (val[0] == "USD"):
                str_humanize[indicator] = "달러"
                lst_query[indicator] = "USD"
                #cursor = idx
                cursor[0] = True
                indicator += 1

            elif (val[0] == "JPY"):
                str_humanize[indicator] = "엔"
                lst_query[indicator] = "JPY"
                #cursor = idx
                cursor[0] = True
                indicator += 1

            elif (val[0] == "EUR"):
                str_humanize[indicator] = "유로"
                lst_query[indicator] = "EUR"
                #cursor = idx
                cursor[0] = True
                indicator += 1

            elif (val[0] == "CNY"):
                str_humanize[indicator] = "위안"
                lst_query[indicator] = "CNY"
                #cursor = idx
                cursor[0] = True
                indicator += 1

            elif (val[0] == "CAD"):
                str_humanize[indicator] = "(캐나다)달러"
                lst_query[indicator] = "CAD"
                #cursor = idx
                cursor[0] = True
                indicator += 1

            elif (val[0] == "RUB"):
                str_humanize[indicator] = "루블"
                lst_query[indicator] = "CAD"
                #cursor = idx
                cursor[0] = True
                indicator += 1

            elif (val[0] == "GBP"):
                str_humanize[indicator] = "파운드"
                lst_query[indicator] = "GBP"
                #cursor = idx
                cursor[0] = True
                indicator += 1

        if (idx - number_cursor) <= 1:
            multiplier = korean_to_number(val[0])

    to_measure = float(value_of_currency * multiplier)


    if (to_measure == 1) and (not indicator <= 1):
        str_humanize.reverse()
        str_query = lst_query[1] + lst_query[0]
    else:
        str_query = lst_query[0] + lst_query[1]

    if lst_query[0] == "JPY" and (to_measure == 1):
        to_measure = 100

    return str_query, to_measure, str_humanize


def korean_to_number(text):

    multiplier = 1
    for val in text:
        if val == "십":
            multiplier *= 10
        elif val == "백":
            multiplier *= 100
        elif val == "천":
            multiplier *= 1000
        elif val == "만":
            multiplier *= 10000
        elif val == "억":
            multiplier *= 100000000
        else:
            multiplier *= 1

    return multiplier


if __name__ == "__main__":
    pass
