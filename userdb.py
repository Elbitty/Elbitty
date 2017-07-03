import sqlite3
import os

FILE_NAME = 'users.db'

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
FULL_PATH = os.path.join(THIS_FOLDER, FILE_NAME)

conn = sqlite3.connect(FULL_PATH)


conn.execute("""CREATE TABLE IF NOT EXISTS users (
	st INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	uid NUMERIC UNIQUE,
	screen_name VARCHAR(15),
	nickname VARCHAR(40),
	is_admin BOOLEAN,
	first_request TEXT,
	first_request_time INTEGER,
	recent_requset TEXT,
	recent_request_time INTEGER,
	today_requests INTEGER,
	total_requests INTEGER
);
""")
conn.close()

FILE_NAME = 'y3.db'

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
FULL_PATH = os.path.join(THIS_FOLDER, FILE_NAME)

conn2 = sqlite3.connect(FULL_PATH)

conn2.execute("""CREATE TABLE IF NOT EXISTS location (
	st INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    tag TEXT UNIQUE,
	address TEXT,
	latitude FLOAT,
	longtitude FLOAT,
	update_time INTEGER,
    etc TEXT
);
""")

conn2.execute("""CREATE TABLE IF NOT EXISTS encyclopedia (
	st INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	tag TEXT UNIQUE,
	name TEXT UNIQUE,
	content TEXT,
    update_time INTEGER,
    etc TEXT
);
""")
conn2.execute("""CREATE TABLE IF NOT EXISTS shopping (
	st INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	tag TEXT UNIQUE,
    maker TEXT,
    name TEXT UNIQUE,
	price_min INTEGER,
	price_max INTEGER,
    update_time INTEGER,
    etc TEXT
);
""")
conn2.execute("""CREATE TABLE IF NOT EXISTS weather (
	st INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    tag TEXT UNIQUE,
	place TEXT UNIQUE,
	content TEXT,
    temperature INTEGER,
	update_time INTEGER,
    etc TEXT
);
""")
conn2.execute("""CREATE TABLE IF NOT EXISTS misedust_pm10 (
	st  INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    tag TEXT UNIQUE,
	place TEXT UNIQUE,
    grade TEXT,
	value INTEGER,
	update_time INTEGER,
    etc TEXT
);
""")

conn2.execute("""CREATE TABLE IF NOT EXISTS currency (
	st INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	tag TEXT UNIQUE,
    from_ TEXT,
    to_ TEXT,
	from_to TEXT,
	value FLOAT,
    update_time INTEGER,
    etc TEXT
);
""")

conn2.close()

print("Opened database successfully")

