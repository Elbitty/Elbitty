#!/usr/bin/env python
# -*- coding:utf-8 -*-

from konlpy.tag import Twitter
twitter = Twitter()

#------------------------------------------------------------------------
def calculate_no_norm(content):
    temp_pos = twitter.pos(content)
    return temp_pos

#------------------------------------------------------------------------
def calculate(content):
    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [None] #* len(TmpPos)

    print(temp_pos)

    temp_morphs = [temp_pos[x][0] for x in range(len(temp_pos))]
    return temp_morphs

#------------------------------------------------------------------------
def calculate_except_josa(content):
    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [] #* len(TmpPos)

    for tmp in temp_pos:
        if tmp[1] == 'Josa':
            temp_pos.remove((tmp[0], tmp[1]))

    print(temp_pos)

    temp_morphs = [temp_pos[x][0] for x in range(len(temp_pos))]
    return temp_morphs

#------------------------------------------------------------------------
def calculate_only_nouns(content):
    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [] #* len(TmpPos)

    for tmp in temp_pos:
        if (tmp[1] == 'Noun') or (tmp[1] == 'Exclamation') or (tmp[1] == 'Alpha') or (tmp[1] == 'Punctuation') or (tmp[1] == 'Number'):
            temp_morphs.append(tmp[0])

    print(temp_morphs)

    return temp_morphs

#------------------------------------------------------------------------
def calculate_also_pos(content):
    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [] #* len(TmpPos)

    for tmp in temp_pos:
        if (tmp[1] == 'Noun') or (tmp[1] == 'Josa') or (tmp[1] == 'Exclamation') or (tmp[1] == 'Alpha') or (tmp[1] == 'Number'):
            #1천원은 몇엔이야? 의 '엔'을 조사로 인식하기에 조사도 포함함.
            temp_morphs.append([tmp[0], tmp[1]])

    print(temp_morphs)

    return temp_morphs

#------------------------------------------------------------------------
def calculate_currency(content):

    temp_calculated = to_calculate_currency(content)
    content = "".join([temp_calculated[x][0] for x in range(len(temp_calculated))])

    content = content.replace("원", " KRW ", 1)
    content = content.replace("엔", " JPY ", 1)
    content = content.replace("유로", " EUR ", 1)
    content = content.replace("위안", " CNY ", 1)
    content = content.replace("루블", " RUB ", 1)
    content = content.replace("파운드", " GBP ", 1)
    content = content.replace("캐나다 달러", " CAD ", 1)
    content = content.replace("캐나다달러", " CAD ", 1)
    content = content.replace("달러", " USD ", 1)
    content = content.replace("캐나다", " CAD ", 1)

    content = content.replace("으", " ")
    content = content.replace("로", " ")
    content = content.replace("은", " ")
    content = content.replace("는", " ")
    content = content.replace("이", " ")
    content = content.replace("가", " ")
    content = content.replace("의", " ")
    content = content.replace("을", " ")
    content = content.replace("를", " ")
    content = content.replace("다", " ")

    content = content.replace("일", " 1 ")
    content = content.replace("이", " 2 ")
    content = content.replace("삼", " 3 ")
    content = content.replace("사", " 4 ")
    content = content.replace("오", " 5 ")
    content = content.replace("육", " 6 ")
    content = content.replace("칠", " 7 ")
    content = content.replace("팔", " 8 ")
    content = content.replace("구", " 9 ")


    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [] #* len(TmpPos)

    trigger = False
    dotted = False

    for tmp in temp_pos:
        if (tmp[1] == 'Noun') or (tmp[1] == 'Exclamation'):
            #1천원은 몇엔이야? 의 '엔'을 조사로 인식하기에 조사도 포함함.
            trigger = False
            temp_morphs.append([tmp[0], tmp[1]])
        elif (tmp[1] == 'Alpha'):
            trigger = False
            temp_morphs.append([tmp[0].upper(),tmp[1]])
        elif (tmp[1] == 'Number'):
            if trigger:
                length = len(temp_morphs) - 1
                temp_morphs[length][0] = temp_morphs[length][0] + tmp[0]
            else:
                trigger = True
                temp_morphs.append([tmp[0].upper(),tmp[1]])
        elif (tmp[0] == '.'):
            if trigger and not dotted:
                length = len(temp_morphs) - 1
                temp_morphs[length][0] = temp_morphs[length][0] + tmp[0]
                dotted = True
            #else:
                #trigger = False
        else:
            trigger = False

    print(temp_morphs)

    return temp_morphs

#------------------------------------------------------------------------
def to_calculate_currency(content):

    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [] #* len(TmpPos)

    trigger = False
    dotted = False

    for tmp in temp_pos:
        if (tmp[1] == 'Noun') or (tmp[1] == 'Exclamation'):
            #1천원은 몇엔이야? 의 '엔'을 조사로 인식하기에 조사도 포함함.
            trigger = False
            temp_morphs.append([tmp[0], tmp[1]])
        elif (tmp[1] == 'Alpha'):
            trigger = False
            temp_morphs.append([tmp[0].upper(), tmp[1]])
        elif (tmp[0] == '엔'):
            trigger = False
            temp_morphs.append([tmp[0], 'Noun'])
        elif (tmp[1] == 'Number'):
            if trigger:
                length = len(temp_morphs) - 1
                temp_morphs[length][0] = temp_morphs[length][0] + tmp[0]
            else:
                trigger = True
                temp_morphs.append([tmp[0].upper(), tmp[1]])
        elif (tmp[0] == '.'):
            if trigger and not dotted:
                length = len(temp_morphs) - 1
                temp_morphs[length][0] = temp_morphs[length][0] + tmp[0]
                dotted = True
            #else:
                #trigger = False
        else:
            trigger = False

    print(temp_morphs)

    return temp_morphs

#------------------------------------------------------------------------
def list_replace(list_content, from_value, to_value):
    for idx, val in enumerate(list_content):
        if val == from_value:
            list_content[idx] = to_value

#------------------------------------------------------------------------
if __name__ == '__main__':
    print(calculate("알려줘"))
