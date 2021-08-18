#!/usr/bin/python

import sqlite3
import datetime
import pandas as pd

def db_connection():
    try:
        conn = sqlite3.connect('test_aquarium.db')
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def create_table():
    conn = sqlite3.connect('test_aquarium.db')
    print ("Opened database successfully")

    conn.execute('''CREATE TABLE SENSORS
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            TEMP_EXT       REAL    ,
            HUM_EXT        REAL     ,
            DATE        TIMESTAMP);''')
    print ("Table created successfully")
    conn.close()

def insert_item(t_ext,h_ext, relevant_table):
    try:
        conn = sqlite3.connect('test_aquarium.db')
        #print ("Opened database successfully")

        data_tuple = (t_ext, h_ext, datetime.datetime.now())
        if (relevant_table=="SENSORS"):
            sqlite_insert_with_param = """INSERT INTO """ + relevant_table + """ (TEMP_EXT,HUM_EXT,DATE) VALUES (?, ?, ?);"""

        conn.execute(sqlite_insert_with_param, data_tuple);
        conn.commit()

        print ("Item Added")
        #print ("Records created successfully")
        conn.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def select_from_db():
    conn = sqlite3.connect('test_aquarium.db')
    #print ("Opened database successfully")

    cursor = conn.execute("SELECT id, TEMP_EXT, HUM_EXT, DATE from SENSORS")
    #for row in cursor:
        #print (datetime.datetime.now())
        #print ("ID = ", row[0])
        #print ("TEMP_EXT = ", row[1])
        #print ("HUM_EXT = ", row[2])
        #print ("DATE = ", row[3], "\n") 

    #print ("Operation done successfully")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_item():
    conn = sqlite3.connect('test_aquarium.db')
    print ("Opened database successfully")

    conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
    conn.commit()
    print ("Total number of rows updated :"), conn.total_changes

    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print ("ID = "), row[0]
        print ("NAME = "), row[1]
        print ("ADDRESS = "), row[2]
        print ("SALARY = "), row[3], "\n"

    print ("Operation done successfully")
    conn.close()

def delete_item():
    conn = sqlite3.connect('test_aquarium.db')
    print ("Opened database successfully")

    conn.execute("DELETE from COMPANY where ID = 2;")
    conn.commit()
    print ("Total number of rows deleted :"), conn.total_changes

    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print ("ID = "), row[0]
        print ("NAME = "), row[1]
        print ("ADDRESS = "), row[2]
        print ("SALARY = "), row[3], "\n"

    print ("Operation done successfully")
    conn.close()


def graph_data_sqlite():
    conn = sqlite3.connect('test_aquarium.db')
    df = pd.read_sql_query("SELECT id, TEMP_EXT, HUM_EXT, DATE from SENSORS", conn)
    df= df.tail(10)
    return df