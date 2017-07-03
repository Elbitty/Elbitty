#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3
import os
import datetime


def isuserlimit(uid, timeout = 4):
    FILE_NAME = 'users.db'
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FULL_PATH = os.path.join(THIS_FOLDER, FILE_NAME)
    conn = sqlite3.connect(FULL_PATH)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT recent_request_time FROM users WHERE uid = " + str(uid) + ";")
        row = cur.fetchone()
        print(row)
        if row != None: #내용이 없지 않다면
            if request_delayed(row[0], timeout): #4분 경과시
                conn.execute("UPDATE users SET recent_request_time = " +\
                                    str(now_int()) + " WHERE uid = " + str(uid) + ";")
                conn.commit()
                answer = False
            else:
                answer = now_time(row[0])
        else:
            conn.execute("INSERT OR REPLACE INTO users(uid, recent_request_time) VALUES (" +\
                                    str(uid) + ", " + str(now_int()) + ");")
            conn.commit()
            answer = False
    conn.close()
    return answer

def isapilimit(api_name, tag, timeout=30):
    FILE_NAME = 'y3.db'
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FULL_PATH = os.path.join(THIS_FOLDER, FILE_NAME)
    conn = sqlite3.connect(FULL_PATH)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT update_time FROM " + api_name + " WHERE tag = '" + str(tag) + "';")
        row = cur.fetchone()
        if row != None: #내용이 있다면
            if request_delayed(row[0], timeout): #30분 경과시
                answer = None
            else:
                cur.execute("SELECT etc FROM " + api_name + " WHERE tag = '" + str(tag) + "';")
                ans = cur.fetchone()
                answer = (ans[0], row[0])
        else:
            conn.execute("INSERT OR REPLACE INTO " + api_name + "(tag, update_time) VALUES ('" +\
                                    str(tag) + "', " + str(now_int()) + ");")
            conn.commit()
            answer = None
    conn.close()
    return answer


def apilimitupdate(api_name, tag, content):
    content = content.replace("'", "''") #injection 방지

    FILE_NAME = 'y3.db'
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    FULL_PATH = os.path.join(THIS_FOLDER, FILE_NAME)
    conn = sqlite3.connect(FULL_PATH)
    with conn:
        conn.execute("UPDATE " + api_name + " SET update_time = " +\
                            str(now_int()) + ", etc = '" + content + "' WHERE tag = '" + tag + "';")
        conn.commit()
    conn.close()
    return


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

def now_time(unix_time):
    return datetime.datetime.fromtimestamp(
        int(unix_time)
    ).strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    isapilimit("encyclopedia", "소니")
    apilimitupdate("encyclopedia", "소니", "ㅁㄴㅇㄹ")
