#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import difflib
from bs4 import BeautifulSoup
import requests

from stringtext import StringProcess

def calculate(query: str) -> str:
    params = {"query" : query}
    html = requests.get("http://terms.naver.com/search.nhn", params=params).text
    soup = BeautifulSoup(html, "lxml")
    content = soup.find_all("ul", "thmb_lst")

    try:
        soup = BeautifulSoup(str(content[0]), "lxml")
    except Exception as exc:
        return "NA"

    q_dl = soup.find_all("dl")
    tmp_a = str(q_dl[0]).split("<a")
    tmp_a = str(tmp_a[1]).split(">")[0]
    title = str(q_dl[0]).split("</a")[0]

    title = title.split("<a" + tmp_a + ">")[1]

    title = StringProcess.multiple_replace(title, ["<strong>", "</strong>"], "")
    title = re.sub(r"\[[^()]*\]", "", title)
    title = title.strip()

    if (difflib.SequenceMatcher(None, query.upper(), title.upper()).ratio() < 0.334):
        return "NA"

    soup = BeautifulSoup(str(content[0]), "lxml")
    dd_dsc = soup.find_all("dd", "dsc")

    final_dd = StringProcess.multiple_replace(str(dd_dsc[0]), ['<dd class="dsc">', '</dd>', '[내용]'], "")
    final_dd = StringProcess.multiple_replace(final_dd, ['<strong>', '</strong>'], "'")

    final_dd = remove_brackets(final_dd)

    final_dd = StringProcess.multiple_replace(final_dd, ['《', '》'])
    final_dd = final_dd.replace('  ', ' ').replace('...', '…').strip()

    final_dd_sentence = []
    if "." in final_dd:
        final_dd_sentence = final_dd.split(".")
    else:
        final_dd_sentence.append(final_dd)

    josa = re.sub(r'\W+', '', title)
    josa = find_josa(StringProcess.right(josa, 1))

    length = int(round(len(final_dd_sentence[0])/3.334, 0))
    to_find_sentence = final_dd_sentence[0][0:length]

    len_of_title = len(title) + 2

    if ("은 " in to_find_sentence) or ("는 " in to_find_sentence) or ("란 " in to_find_sentence):
        pass
    else:
        if StringProcess.left(final_dd, len_of_title) == ("'" + title + "'"):
            final_dd = StringProcess.right(final_dd, len(final_dd) - len_of_title)
        final_dd = "'" + title + "'" + josa + " " + final_dd

    if len(final_dd_sentence) > 1:
        final_dd = final_dd.split(".")[0]
        #final_dd = final_dd.replace(final_dd_sentence[len(final_dd_sentence)-1], "")

    if StringProcess.right(final_dd, 1) == "다":
        if StringProcess.right(final_dd, 2) == "이다":
            final_dd = StringProcess.left(final_dd, len(final_dd)-2)
        elif StringProcess.right(final_dd, 3) == "합니다":
            final_dd = StringProcess.left(final_dd, len(final_dd)-3) + "함"
        elif StringProcess.right(final_dd, 3) == "입니다":
            final_dd = StringProcess.left(final_dd, len(final_dd)-3)
        else:
            final_dd = StringProcess.left(final_dd, len(final_dd)-1)

    if StringProcess.left(final_dd, 2) == "한편":
        final_dd = StringProcess.right(final_dd, len(final_dd)-2)

    final_dd = final_dd.replace("''", "'").replace("  ", " ").strip()

    return final_dd



def find_josa(text, case_trail="은", case_no_trail="는"):
    text = StringProcess.right(text, 1).upper()

    if re.search(r"^[A-Za-z0-9]+$", text) is not None:
        print(re.search(r"^[A-Za-z0-9]+$", text))
        if text is "L" or text is "M" or text is "N" or text is "R":
            return case_trail
        elif text is "0" or text is "1" or text is "3" or text is "6" or text is "7" or text is "8":
            return case_trail
        else:
            return case_no_trail

    if StringProcess.last_word(text) == 0:
        return case_no_trail
    else:
        return case_trail


def remove_brackets(text):
    while ("(" in text) and (")" in text):
        text = re.sub(r"\([^()]*\)", "", text)
    return text


if __name__ == "__main__":
    print(calculate("ot"))
