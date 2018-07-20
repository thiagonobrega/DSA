#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 12:06:40 2018

@author: thiagonobrega
"""

#from mysql.connector import (connection)
import mysql.connector

config = {
  'user': 'thiago',
  'password': 'agr123',
  'host': '200.129.73.195',
  'database': 'mysql',
  'raise_on_warnings': True,
}

try:
    #CREATE USER 'thiago'@'200.129.73.%' IDENTIFIED BY 'agr123';
    #SET PASSWORD FOR thiago@'200.129.73.%' = PASSWORD('agr123);
    #GRANT SELECT,SHOW DATABASES on *.* to thiago@'200.129.73.%'
    #GRANT SHOW DATABASES on *.* to 'thiago'@'200.129.73.%';
    #cnx = connection.MySQLConnection(user='scott', password='password',host='127.0.0.1',database='employees')
    #SELECT TABLE_SCHEMA, TABLE_NAME, TABLE_TYPE, ENGINE FROM information_schema.TABLES;
    cnx = mysql.connector.connect(**config)
    
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
else:
    cursor = cnx.cursor()
    #cursor.execute("SELECT DISTINCT(Db) FROM mysql.db;")
    cursor.execute("SHOW DATABASES")
    #cursor.execute("SELECT DISTINCT(TABLE_SCHEMA) FROM information_schema.TABLES;")
    
    databases = []
    
    for i in cursor:
        dbt = i[0]#.decode("utf-8")
        databases.append(dbt)
        
        
    cnx.close()
    
    #SELECT TABLE_SCHEMA,TABLE_NAME,ENGINE FROM information_schema.TABLES;
    
    
    #select * from information_schema.user_privileges;