#!/usr/bin/env python
# -*- coding:utf-8 -*-

from konlpy.tag import Twitter
twitter = Twitter()


def calculate(content):
    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [None] #* len(TmpPos)

    print(temp_pos)

    temp_morphs = [temp_pos[x][0] for x in range(len(temp_pos))]
    return temp_morphs


def calculate_except_josa(content):
    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [] #* len(TmpPos)

    for tmp in temp_pos:
        if tmp[1] == 'Josa':
            temp_pos.remove((tmp[0], tmp[1]))

    print(temp_pos)

    temp_morphs = [temp_pos[x][0] for x in range(len(temp_pos))]
    return temp_morphs


def calculate_only_nouns(content):
    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [] #* len(TmpPos)

    for tmp in temp_pos:
        if (tmp[1] == 'Noun') or (tmp[1] == 'Exclamation') or (tmp[1] == 'Alpha') or (tmp[1] == 'Number'):
            temp_morphs.append(tmp[0])

    print(temp_morphs)

    return temp_morphs

def calculate_also_pos(content):
    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [] #* len(TmpPos)

    for tmp in temp_pos:
        if (tmp[1] == 'Noun') or (tmp[1] == 'Josa') or (tmp[1] == 'Exclamation') or (tmp[1] == 'Alpha') or (tmp[1] == 'Number'):
            #1천원은 몇엔이야? 의 '엔'을 조사로 인식하기에 조사도 포함함.
            temp_morphs.append([tmp[0], tmp[1]])

    print(temp_morphs)

    return temp_morphs

def calculate_also_en(content):
    temp_pos = twitter.pos(content, norm=True, stem=True)
    temp_morphs = [] #* len(TmpPos)

    for tmp in temp_pos:
        if (tmp[1] == 'Noun') or (tmp[0] == '엔') or (tmp[1] == 'Exclamation') or (tmp[1] == 'Number'):
            #1천원은 몇엔이야? 의 '엔'을 조사로 인식하기에 조사도 포함함.
            temp_morphs.append(tmp[0])
        elif (tmp[1] == 'Alpha'):
            temp_morphs.append(tmp[0].upper())

    print(temp_morphs)

    return temp_morphs

if __name__ == '__main__':
    print(calculate_also_en("50JPy는 몇엔이야"))
