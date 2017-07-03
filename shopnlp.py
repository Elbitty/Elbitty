"""

by @_circonor

"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shopping
from stringtext import StringProcess
import NLP


class ShopNLP:
    """

    Item(Goods) NLP Implementation
    by @_circonor

    """
    @property
    def loads(self):
        """분석할 구문의 입력 값입니다."""
        return self.__loads

    @loads.setter
    def loads(self, to_load):
        """
        분석할 구문의 입력 값입니다.

            to_load: 분석할 list, 혹은 str.
        """
        if isinstance(to_load, list) is True:
            self.__loads = to_load
        elif isinstance(to_load, str) is True:
            self.__loads = NLP.calculate_only_nouns(to_load)

    def __init__(self, to_load=None):
        """
        객체의 생성자.

            to_load: 분석할 list, 혹은 str.
        """
        self.__maker = str('') #상품의 메이커
        self.__title = str('') #상품명
        self.__price_min = int(0) #최소가
        self.__price_max = int(0) #최대가
        if to_load != None:
            self.__loads = to_load
        else:
            self.__loads = []
        return

    def __item_step(self, list_to_step):
        """List 형 객체 내의 item을 1개 부터 총 item의 갯수 까지 차례대로 추출하여 합성합니다.
        접근 제어 수준은 private입니다."""
        temp_stepped_list = \
            [ \
                ' '.join(str(val)\
                 for val in list_to_step[:idx + 1 or None]) \
                    for idx in range(len(list_to_step)) \
            ]
        return temp_stepped_list

    def get(self):
        """상품명과 관련된 어휘만 추출하여 가져옵니다."""
        first_analyzed_tags = self.__loads

        finalized_goodname = None # 변수 초기화

        if len(first_analyzed_tags) > 0: # 태그가 1개 이상 있다면
            tag_analyzed_words = self.__item_step(first_analyzed_tags) # step별로 차례대로 합성한다.

            for word in tag_analyzed_words:
                calcuated_word = shopping.calculate(word) # 하나씩 찾기
                if calcuated_word is not False: # 찾는 단어가 존재한다면
                    finalized_goodname = calcuated_word
                    #print(word)
                else: # 존재하지 않는 시점에서 break로 루프 탈출
                    break

        if finalized_goodname is None:
            return False

        self.__maker = finalized_goodname[0]
        self.__title = finalized_goodname[1]
        self.__price_min = finalized_goodname[2]
        self.__price_max = finalized_goodname[3]

        return True

    #getter
    @property
    def maker(self):
        """
        상품의 메이커를 가져옵니다.

            return: str 형의 '상품의 메이커'를 반환합니다.
        """
        return self.__maker

    @property
    def name(self):
        """
        상품명을 가져옵니다.

             return: str 형의 상품명을 반환합니다.
        """
        return self.__title

    @property
    def price(self):
        """
        상품의 가격을 가져옵니다.

             return: tuple(int, int) 형의 상품의 최저가, 상품의 최고가를 반환합니다.
        """
        return self.__price_min, self.__price_max

    @property

    def price_min(self):
        """
        상품의 최저가를 가져옵니다.

             return: int 형의 상품의 최저가를 반환합니다.
        """
        return self.__price_min

    @property
    def price_max(self):
        """
        상품의 최고가를 가져옵니다.

             return: int 형의 상품의 최고가를 반환합니다.
        """
        return self.__price_max
