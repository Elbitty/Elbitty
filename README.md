# Elbitty
https://github.com/Elbitty/Elbitty

https://twitter.com/HiElbitty

대화형 트위터 봇인 Elbitty는 유저의 멘션을 읽고, 그에 대한 다양한 정보를 실시간으로 알려 드립니다. 

----

용례
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

Elbitty는 신뢰할 수 있는 출처에서만 정보를 가져오며, 다음과 같습니다.

| 정보 | 출처 | 웹사이트 |비고|
| :-- | :--- | :-------- | :-- |
|위치|Google Maps|[maps.google.com](https://www.google.com/maps)||
|날씨|OpenWeatherMap|[openweathermap.org](https://openweathermap.org/)||
|미세먼지|SK planet DEVELOPERS|[developers.skplanetx.com](https://developers.skplanetx.com/)||
|환율|Yahoo Finance|[finance.yahoo.com](https://finance.yahoo.com/)|with [YQL](https://developer.yahoo.com/yql/)|
|정보|NAVER 지식백과|[terms.naver.com](http://terms.naver.com/)||
|쇼핑|DAUM 쇼핑하우|[shopping.daum.net](http://shopping.daum.net/)|via [DAUM Developers](http://developers.daum.net)|


면책 사항
----------

### 아래의 면책 사항을 주의 깊게 확인하여 주십시오. 

1. Elbitty는 사용자의 요청에 따라 정보를 가져와 보여주는 단순 중개 역할만을 합니다. 
2. Elbitty가 알려드리는 정보를 맹신하지 마십시오. Elbitty는 무료, 무상의 서비스입니다. Elbitty로 인하여 발생되는 피해나 손실, 손해의 책임은 전적으로 사용자에게 있습니다. 
3. 귀하의 상세한 위치 정보를 Elbitty에게 전송하지 마십시오. Twitter는 열려 있는 소셜 네트워크 서비스이므로, 알려진 위치로 인해 현실에서 피해를 입을 가능성이 있습니다. 
