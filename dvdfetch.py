# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:37:29 2024

@author: ADMIN
"""
##################################################################
#After installing with pip install psycopg2
import psycopg2 as pg2

#Create a connection with PostgreSQL
#'password' is whatever you set,we set password
conn=pg2.connect(database='dvdrental',user='postgres',password='student')

#Establish connection and start curser to be ready to query
cur=conn.cursor()

#pass in a PostgreSQL quary as a string
cur.execute("SELECT * FROM payment")

#Return a tuple of the first row as Python objects
cur.fetchone()

#Return N number of rows
cur.fetchmany(10)

#Return ALl rows at once
cur.fetchall()

#To save and index results,assing it to a variable
data=cur.fetchmany(10)

conn.close()




