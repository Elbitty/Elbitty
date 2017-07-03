#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3
import os
import datetime
from locnlp import LocNLP

def getlocationdb(tag):
    n_text = " ".join(str(val) for val in tag)

    FILE_NAME = 'y3.db'
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FULL_PATH = os.path.join(THIS_FOLDER, FILE_NAME)
    conn = sqlite3.connect(FULL_PATH)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT update_time FROM location WHERE tag = '" + n_text + "';")
        row = cur.fetchone()
        if row != None: #내용이 있다면
            if request_delayed(row[0], 20160): #14일 경과시
                print("loc_1")
                loc_tag = LocNLP()
                loc_tag.loads = n_text
                loc_tag.get()

                addr = loc_tag.address
                latt = loc_tag.latitude
                longt = loc_tag.longitude

                conn.execute("UPDATE location SET update_time = " + str(now_int()) + ", address = '" + addr + "' WHERE tag = '" + n_text + "';")
                conn.execute("UPDATE location SET update_time = " + str(now_int()) + ", latitude = '" + str(latt) + "' WHERE tag = '" + n_text + "';")
                conn.execute("UPDATE location SET update_time = " + str(now_int()) + ", longtitude = '" + str(longt) + "' WHERE tag = '" + n_text + "';")
                conn.commit()
                answer = (addr, latt, longt)
            else:
                print("loc_2")
                cur.execute("SELECT address FROM location WHERE tag = '" + n_text + "';")
                addr = cur.fetchone()
                cur.execute("SELECT latitude FROM location WHERE tag = '" + n_text + "';")
                latt = cur.fetchone()
                cur.execute("SELECT longtitude FROM location WHERE tag = '" + n_text + "';")
                longt = cur.fetchone()

                answer = (addr[0], latt[0], longt[0])
        else:
            print("loc_3")
            loc_tag = LocNLP()
            loc_tag.loads = tag
            loc_tag.get()

            addr = loc_tag.address
            latt = loc_tag.latitude
            longt = loc_tag.longitude

            conn.execute("INSERT OR REPLACE INTO location(tag, update_time, address, latitude, longtitude) VALUES ('" +
                         n_text + "', " + str(now_int()) + ", '" + addr + "', " + str(latt) + ", " + str(longt) + ");")
            conn.commit()
            answer = (addr, latt, longt)
    conn.close()
    return answer

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
    print(getlocationdb("대전 중구"))
