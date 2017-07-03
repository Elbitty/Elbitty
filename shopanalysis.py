#!/usr/bin/env python
# -*- coding:utf-8 -*-

from shopnlp import ShopNLP
from stringtext import StringProcess

def calculate(keyword_tags):
    shopnlp = ShopNLP()
    shopnlp.loads = keyword_tags
    shopnlp.get()

    name = (shopnlp.name).strip()
    maker = (shopnlp.maker).strip()
    price_min = shopnlp.price_min
    price_max = shopnlp.price_max

    if StringProcess.left(name, len(maker)) == maker:
        name = StringProcess.right(name, len(name)-len(maker))

    name = name.replace('\n', ' ')

    if (maker != "") and (name != ""):
        temp_str = maker + name + "의 가격은 " + str(price_min) + " 원 ~ " + str(price_max) + " 원" #"이에요."
    else:
        temp_str = "NA"

    return temp_str


if __name__ == '__main__':
    print(calculate("소니 a6500"))
