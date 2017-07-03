#!/usr/bin/env python
# -*- coding:utf-8 -*-


from stringtext import StringProcess
import NLP

def calculate(query: str) -> str:

    NLPd = NLP.calculate_only_nouns(query)

    is_available = True

    while is_available:
        length = len(NLPd)-1
        if length > 0:
            if NLPd[length] == "좀":
                NLPd.pop()
                is_available = True

            elif NLPd[length] == "정보":
                NLPd.pop()
                is_available = True

            elif NLPd[length] == "관련":
                NLPd.pop()
                is_available = True

            elif (NLPd[length] == "대한") or (NLPd[length] == "대해"):
                NLPd.pop()
                is_available = True

            elif ((NLPd[length-1] == "무엇") or (NLPd[length-1] == "뭐") or (NLPd[length-1] == "누구")) and (NLPd[length] == "인지"):
                NLPd.pop()
                NLPd.pop()
                is_available = True

            elif (NLPd[length] == "무엇") or (NLPd[length] == "뭐") or (NLPd[length] == "누구"):
                NLPd.pop()
                is_available = True

            elif NLPd[length] == "과연":
                NLPd.pop()
                is_available = True

            elif NLPd[length] == "란":
                NLPd.pop()
                is_available = True

            elif NLPd[length] == "장르":
                NLPd.pop()
                is_available = True

            else:
                is_available = False
        else:
            is_available = False

    to_split = len(NLPd)-1
    query = query.split(NLPd[to_split])[0] + NLPd[to_split]

    query = StringProcess.multiple_replace(
        query, [",", '"', "'", "`", "(", ")", "=", "--", "/", '\\', ";", "*", "?"]
        ).strip().upper()

    r_q = NLP.calculate_no_norm(query)
    tmpr = str("")

    for val in r_q:
        if (val[1] == "Josa") or (val[1] == "Eomi") or\
         (val[1] == "Punctuation") or (val[1] == "Alpha") or (val[1] == "Number"):
            tmpr = tmpr + val[0]
        else:
            tmpr = tmpr + " " + val[0]

    return tmpr


if __name__ == "__main__":
    print(calculate("C++에대해서알려주세요"))
