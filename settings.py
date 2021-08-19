#!/usr/bin/env python3

import configparser

def settings_read_database_mysql():
    config = configparser.ConfigParser()
    config.read('settings.ini')

    mysql={}

    mysql['username'] = config['mysql']['username']
    mysql['password'] = config['mysql']['password']
    mysql['database'] = config['mysql']['database']

    return mysql
   
def settings_write_database_mysql(username, password, database):
    config = configparser.ConfigParser()
    config.read("settings.ini")

    #config.add_section('mysql')

    config['mysql']['username'] = username
    config['mysql']['password'] = password
    config['mysql']['database'] = database
    

    with open('settings.ini', 'w') as configfile:
        config.write(configfile)

def settings_read_email():
    config = configparser.ConfigParser()
    config.read('settings.ini')

    email={}

    email['username'] = config['email']['username']
    email['password'] = config['email']['password']
    email['port'] = config['email']['port']

    return email
   

def settings_write_email(username, password, port):
    config = configparser.ConfigParser()
    config.read("settings.ini")

    #config.add_section('email')

    config['email']['username'] = username
    config['email']['password'] = password
    config['email']['port'] = port
    

    with open('settings.ini', 'w') as configfile:
        config.write(configfile)