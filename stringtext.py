"""
문자열을 다루는 클래스인 StringProcess 클래스가 포함된 모듈입니다.
"""

#!/usr/bin/env python
# -*- coding:utf-8 -*-

class StringProcess:
    """
    string 형의 객체를 처리합니다.

        static 인 right(), left()를 포함합니다.
    """

    @staticmethod
    def right(text, count=1):
        """
        문자열의 오른쪽부터 문자열을 가져옵니다.

            text: 나눠질 대상 str 입니다.
            count: 가져올 개수 int 입니다.
        """
        text_length = len(text)
        return text[text_length-(count):text_length]

    @staticmethod
    def left(text, count=1):
        """
        문자열의 왼쪽부터 문자열을 가져옵니다.

            text: 나눠질 대상 str 입니다.
            count: 가져올 개수 int 입니다.
        """
        return text[0:count]

    @staticmethod
    def remove_last(text, count=1):
        """
        문자열의 오른쪽 문자열을 제거합니다.

            text: 대상 str 입니다.
            count: 제거할 개수 int 입니다.
        """
        return text[0:-count]

    @staticmethod
    def last_word(letter):
        """
        문자에 종성이 있는지 확인합니다.

            letter: 종성이 있는지 확인 할 str 1 개.
        """
        in_code = int(0)
        code = int(0)
        in_code = ord(letter)
        code = in_code

        if in_code == -1:
            if in_code < 44032:
                return 0
        elif (in_code == 1)or(in_code == 0):
            return 0

        code = code - 44032
        code = code % (21 * 28)
        last = code % 28

        return last

    @staticmethod
    def korean_number(to_calculate):
        danwi = ["만", "억", "조", "경", "해"]
        danwi.reverse()
        total_count_of_danwi = len(danwi)
        tmp_str = str("")
        for idx, val in enumerate(danwi):

            mul = (10**((total_count_of_danwi-idx)*4))

            if to_calculate >= mul:
                tmpv = int((to_calculate - (to_calculate %  mul)) /  mul)
                to_calculate = to_calculate % mul
                tmp_str = tmp_str + "{:,.0f}".format(tmpv) + val + " "

        to_calculate = round(to_calculate, 2)
        if to_calculate != 0:
            if (to_calculate % 1) == 0:
                tmp_str = tmp_str + "{:,.0f}".format(to_calculate)
            else:
                tmp_str = tmp_str + "{:,.2f}".format(to_calculate)

        tmp_str = tmp_str.rstrip()
        return tmp_str


    @staticmethod
    def korean_to_number(text):
        danwi_major = ["만", "억", "조", "경", "해"]
        danwi_minor = ["십", "백", "천"]
        danwi_count = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
        number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        temp_str = ""
        temp_sum = 0
        temp_minor = 0

        for cursor in text:

            if cursor in number:
                temp_str = temp_str + cursor

            elif cursor in danwi_count:
                for idx, count in enumerate(danwi_count):
                    if cursor == count:
                        temp_minor = idx
                        break

            elif cursor in danwi_minor:
                pass


            elif cursor in danwi_major:
                pass





    @staticmethod
    def multiple_replace(text: str, from_list: list, to_str: str="") -> str:
        for val in from_list:
            text = text.replace(val, to_str)

        return text


if __name__ == '__main__':
    VALUE = "31.50"
    print(StringProcess.korean_number(50000))
