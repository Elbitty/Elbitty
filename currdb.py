#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3
import os
import datetime

def getcurrndb(tag):

    FILE_NAME = 'y3.db'
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FULL_PATH = os.path.join(THIS_FOLDER, FILE_NAME)
    conn = sqlite3.connect(FULL_PATH)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT update_time FROM currency WHERE tag = '" + tag + "';")
        row = cur.fetchone()
        if row != None: #내용이 있다면
            if request_delayed(row[0], 30): #30분 경과시
                print("cur_1")
                answer = None
            else:
                print("cur_2")
                cur.execute("SELECT bid_value FROM currency WHERE tag = '" + tag + "';")
                bid = cur.fetchone()
                cur.execute("SELECT ask_value FROM currency WHERE tag = '" + tag + "';")
                ask = cur.fetchone()
                answer = (float(bid[0]), float(ask[0]), row[0])
        else:
            print("cur_3")
            conn.execute("INSERT OR REPLACE INTO currency(tag, update_time) VALUES ('" +
                         tag + "', " + str(now_int()) + ");")
            conn.commit()
            answer = None
    conn.close()
    return answer

def updatedata(tag, bid, ask):
    bid = str(bid)
    ask = str(ask)
    FILE_NAME = 'y3.db'
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FULL_PATH = os.path.join(THIS_FOLDER, FILE_NAME)
    conn = sqlite3.connect(FULL_PATH)
    tmp_str = "SELECT update_time FROM currency WHERE tag = '" + tag + "';"
    with conn:
        cur = conn.cursor()
        cur.execute(tmp_str)
        row = cur.fetchone()
        conn.execute("UPDATE currency SET update_time = " + str(now_int()) + ", bid_value = " + bid + ", ask_value = " + ask + " WHERE tag = '" + tag + "';")
        conn.commit()


def request_delayed(last_request_time, delay):
    if isinstance(last_request_time, tuple):
        if (now_int() - int(last_request_time[0])) > (delay*60):
            return True
        else:
            return False
    else:
        if (now_int() - int(last_request_time)) > (delay*60):
            return True
        else:
            return False

def now_int():
    return int(datetime.datetime.now().timestamp())


if __name__ == "__main__":
    print()