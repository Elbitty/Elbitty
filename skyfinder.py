#!/usr/bin/env python
# -*- coding:utf-8 -*-

from skyscanner.skyscanner import Flights


def calculate():
    flights_service = Flights('eu852557966948323012893595909615')
    result = flights_service.get_result(
        country='UK',
        currency='GBP',
        locale='en-GB',
        originplace='SIN-sky',
        destinationplace='KUL-sky',
        outbounddate='2017-05-28',
        inbounddate='2017-05-31',
        adults=1).parsed


if __name__ == "__main__":
    calculate()
