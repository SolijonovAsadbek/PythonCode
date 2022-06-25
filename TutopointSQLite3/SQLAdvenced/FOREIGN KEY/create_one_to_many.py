import sqlite3

conn = sqlite3.connect('example.db')
query = ('''CREATE TABLE IF NOT EXISTS DOCTOR
    (ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    PHONE_NUMBER CHAR(20) NOT NULL ,
    TYPE TEXT);''')

conn.execute(query)

query = ('''CREATE TABLE IF NOT EXISTS PATIENT
(ID INTEGER PRIMARY KEY ,
NAME TEXT NOT NULL ,
EMAIL_ADDRESS TEXT NOT NULL ,
PHONE_NUMBER CHAR(20) NOT NULL ,
problem CHAR(20) NOT NULL ,
DOCTOR_ID INTEGER NOT NULL ,
FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR (ID))''')

conn.execute(query)

conn.close()