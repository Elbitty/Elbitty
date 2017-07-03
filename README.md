# Elbitty
https://github.com/Elbitty/Elbitty

https://twitter.com/HiElbitty

대화형 트위터 봇인 Elbitty는 유저의 멘션을 읽고, 그에 대한 다양한 정보를 실시간으로 알려 드립니다. 

----

사용 예
----------
Elbitty가 인식할 수 있는 어휘와 구문은 다음과 같습니다.

- 날씨
  - 날씨 알려줘.
    - 기본 위치(서울특별시)의 현재 날씨를 알려 드립니다.
    - 사용자가 즐겨 찾는 위치를 기반으로 기본 위치를 파악하도록 구현할 예정.
  - 지금 날씨 어때?
    - 기본 위치의 현재 날씨를 알려 드립니다.
  - 청담동은 맑은가?
    - '서울특별시 강남구 청담동'의 현재 날씨를 알려 드립니다.
  - 에펠탑 주변의 날씨좀.
    - '프랑스 파리 에펠탑'의 현재 날씨를 알려 드립니다.
    - 이 외에 명소, 상호명, 도로명 주소 기준으로도 인식할 수 있습니다.
  - forecast 추가 예정.
- 미세먼지
  - 미세먼지 어때?
  - 서초구 미세먼지는?
  - 국회의사당 주변 미세먼지.
    - 상동.
- 환율
  - 환율좀 알려주세요.
    - 현시점 기준의 기본 환율(1 USD to KRW)을 알려 드립니다.
  - 천달러가 얼마야?
    - 1000 USD가 몇 KRW인지 알려 드립니다.
  - 3.5만엔이 몇 달러예요?
    - 35000 JPY가 몇 USD인지 알려 드립니다.
- 정보
  - 인공지능에 대해서 알려줘.
  - NLP가 뭐지?
- 쇼핑
  - 린넨 블라우스는 얼마정도 해?
  - A6500 가격 알려줘.


추가 예정인 기능
----------
- 호텔 / 항공권
- 단문 번역기
- Reminder


정보 출처
----------

Elbitty는 신뢰할 수 있는 출처에서만 정보를 가져오며, 각 출처는 다음과 같습니다.

- 날씨
  - OpenWeatherMap(https://openweathermap.org)
- 미세먼지
  - SK planet DEVELOPERS(https://developers.skplanetx.com)
- 환율
  - Yahoo Finance(https://finance.yahoo.com) with YQL(https://developer.yahoo.com/yql/)
- 정보
  - NAVER 지식백과(http://terms.naver.com)
- 쇼핑
  - DAUM 쇼핑하우(http://shopping.daum.net) via DAUM Developers(http://developers.daum.net)
