"""
자연어 처리(Natural Language Process) 기반 한국어 지명 추출 모듈입니다.

자연어 처리를 위한 메인 클래스인 LocNLP 클래스를 포함하고 있습니다.
Made by @_circonor(Twitter)
"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import location
from stringtext import StringProcess
import NLP


class LocNLP:
    """
    한국어 구문에서 지역과 관련된 어휘만 추출하는 분석기입니다.

        loads에 평문 str, 혹은 NLP로 분해된 문자열로 구성된 list 를 set한 뒤, get() 메서드를 통해 지역 관련 어휘만 추출합니다.
        address 프로퍼티에는 해당 지역의 정확한 주소, lattitude 프로퍼티에는 위도, longtitude 프로퍼티에는 경도가 반환됩니다.
    """

    @property
    def default(self):
        """태그 내에 지역이 없다면 찾아 낼 기본값입니다."""
        return self.__default

    @default.setter
    def default(self, value):
        """
        태그 내에 지역이 없다면 찾아 낼 기본값입니다.

            value: 기본값 str.
        """
        self.__default = value

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
        self.__loc = str('')
        self.__latt = float(0)
        self.__longt = float(0)
        self.__default = "서울특별시"
        if to_load != None:
            self.__loads = to_load
        else:
            self.__loads = []
        return

    def __item_step(self, list_to_step):
        """List 형 객체 내의 item을 1개 부터 총 item의 갯수 까지 차례대로 추출하여 합성합니다.
        접근 제어 수준은 private입니다."""
        #tmp_stepped_item_list = []
        #for i in range(0, len(list_to_step)):
        #    tmp_stepped_item_list.append(' '.join(str(e) for e in list_to_step[:i + 1 or None]))
        temp_stepped_list = \
            [ \
                ' '.join(str(val) for val in list_to_step[:idx + 1 or None]) \
                    for idx in range(len(list_to_step)) \
            ]
        return temp_stepped_list


    def __get_only_loc_tags(self, to_get):
        """지역과 관련된 어휘를 1차로 가져옵니다.
        접근 제어 수준은 private입니다."""
        NLP_PLACE = ["서울", "충북", "충남", "경북", "경남", "전북", "전남", "강원", "경기", "제주", \
            "대전", "대구", "부산", "광주", "울산", "인천"]
        NLP_EOMI = ["국", "도", "주", "성", "현", "시", "군", "구", "동", "읍", "면", "리"]
        indicator = 0
        temp_tags = []
        for one_of_tag in to_get:
            if one_of_tag in NLP_PLACE:
                temp_tags.append(one_of_tag)
                indicator = 1
            elif StringProcess.right(one_of_tag) in NLP_EOMI:
                temp_tags.append(one_of_tag)
                indicator = 1
            else:
                if indicator == 1:
                    break
        return temp_tags


    def get(self):
        """지역과 관련된 어휘만 추출하여 가져옵니다."""
        first_analyzed_area_tags = self.__loads

        finalized_location = None

        if len(first_analyzed_area_tags) > 0:
            tag_analyzed_words = self.__item_step(first_analyzed_area_tags)

            for word in tag_analyzed_words:
                if location.calculate(word) is not False:
                    finalized_location = location.calculate(word)
                    print(word)
                else:
                    break

        if finalized_location is None:
            finalized_location = location.calculate(self.__default)

        self.__loc = finalized_location[0]
        self.__latt = finalized_location[1]
        self.__longt = finalized_location[2]

        return True

    #getter
    @property
    def address(self):
        """
        주소를 가져옵니다.

            return: str 형의 주소를 반환합니다.
        """
        return self.__loc

    @property
    def latitude(self):
        """
        위도를 가져옵니다.

             return: float 형의 위도를 반환합니다.
        """
        return self.__latt

    @property
    def longitude(self):
        """
        경도를 가져옵니다.

             return: float 형의 경도를 반환합니다.
        """
        return self.__longt


if __name__ == '__main__': #테스트 메서드
    locnlp = LocNLP()
    locnlp.loads = "서울특별시 시공조아"
    locnlp.get()
    aa = locnlp.address
    print(aa)
