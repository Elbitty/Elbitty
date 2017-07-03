#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3
import os

FILE_NAME = 'y3.db'

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
FULL_PATH = os.path.join(THIS_FOLDER, FILE_NAME)

def db_new(table, col, content):
    if isinstance(content, str):
        tmp_str = "INSERT OR REPLACE INTO " + table + "(" + col + ") VALUES ('" + content + "');"
    else:
        tmp_str = "INSERT OR REPLACE INTO " + table + "(" + col + ") VALUES (" + str(content) + ");"
    print(tmp_str)
    return tmp_str

def db_read(table, to_find, col, content):
    if isinstance(content, str):
        tmp_str = "SELECT " + to_find + " FROM " + table + " WHERE " + col + " = '" + content + "';"
    else:
        tmp_str = "SELECT " + to_find + " FROM " + table + " WHERE " + col + " = " + str(content) + ";"
    print(tmp_str)
    return tmp_str


def do(syntax):
    print(syntax)
    conn = sqlite3.connect(FULL_PATH)
    with conn:
        cur = conn.cursor()
        cur.execute(syntax)
        row = cur.fetchone()
        conn.commit()
    conn.close()
    print(row)
    return row

def new(table, col, content):
    conn = sqlite3.connect(FULL_PATH)
    with conn:
        cur = conn.cursor()
        cur.execute(db_new(table, col, content))
    conn.close()
    return



def find(table, to_find, col, content):
    conn = sqlite3.connect(FULL_PATH)
    with conn:
        cur = conn.cursor()
        cur.execute(db_read(table, to_find, col, content))
        row = cur.fetchone()
    conn.close()
    print(row)
    return row

if __name__ == "__main__":
    print(find('weather', '*', 'place', '오늘'))
