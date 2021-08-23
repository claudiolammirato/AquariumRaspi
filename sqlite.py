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
    #print ("Opened database successfully")

    conn.execute('''CREATE TABLE IF NOT EXISTS SENSORS_EXT
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            TEMP_EXT       REAL    ,
            HUM_EXT        REAL     ,
            DATE        TIMESTAMP);''')
    conn.execute('''CREATE TABLE IF NOT EXISTS SENSORS_INT
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            TEMP_INT       REAL    ,
            DATE        TIMESTAMP);''')
    #print ("Table created successfully")
    print("Database OK!")
    conn.close()

def insert_item(t_ext,h_ext,t_int, relevant_table):
    try:
        conn = sqlite3.connect('test_aquarium.db')
        #print ("Opened database successfully")
        if (t_int == 999):

            data_tuple = (t_ext, h_ext, datetime.datetime.now())
            if (relevant_table=="SENSORS_EXT"):
                sqlite_insert_with_param = """INSERT INTO """ + relevant_table + """ (TEMP_EXT,HUM_EXT,DATE) VALUES (?, ?, ?);"""

            conn.execute(sqlite_insert_with_param, data_tuple);
            conn.commit()

            print ("Item Added")
            #print ("Records created successfully")
            conn.close()
        if (t_ext == 999):
            data_tuple = (t_int, datetime.datetime.now())
            if (relevant_table=="SENSORS_INT"):
                sqlite_insert_with_param = """INSERT INTO """ + relevant_table + """ (TEMP_INT,DATE) VALUES (?, ?);"""

            conn.execute(sqlite_insert_with_param, data_tuple);
            conn.commit()

            print ("Item Added")
            #print ("Records created successfully")
            conn.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def select_from_db_ext_sensor():
    conn = sqlite3.connect('test_aquarium.db')
    #print ("Opened database successfully")

    cursor = conn.execute("SELECT id, TEMP_EXT, HUM_EXT, DATE from SENSORS_EXT")
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

def select_from_db_int_sensor():
    conn = sqlite3.connect('test_aquarium.db')
    #print ("Opened database successfully")

    cursor = conn.execute("SELECT id, TEMP_INT, DATE from SENSORS_INT")
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


def graph_data_sqlite_ext():
    conn = sqlite3.connect('test_aquarium.db')
    df = pd.read_sql_query("SELECT id, TEMP_EXT, HUM_EXT, DATE from SENSORS_EXT", conn)

    #Numero di valori
    #df= df.tail(15)
    return df

def graph_data_sqlite_int():
    conn = sqlite3.connect('test_aquarium.db')
    df = pd.read_sql_query("SELECT id, TEMP_INT, DATE from SENSORS_INT", conn)

    #Numero di valori
    #df= df.tail(15)
    return df