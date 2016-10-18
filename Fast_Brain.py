#1) Testing the "Fast_Brain" connection to db
#2) inputing an int
#
#DATABASE SCHEMA
#Database => Prime-Time-Project
#Table => UserInput
#Column=> num
#

import mysql.connector
from mysql.connector import errorcode

#First we must connect to the db and give error messages when we hit issues
try:
    key = mysql.connector.connect(
        user='root', #MySQL user name
        password='1991', #my connection password
        host='localhost',
        database='Prime-Time-Project')
    print ("Connected to Database!") #success

except mysql.connector.Error as e: #fail ... what's the issue?
   if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
       print("Something is wrong with the username or password")
   elif e.errno == errorcode.ER_BAD_DB_ERROR:
       print("Database doesn't exist")
   else:
       print(e)

mycursor = key.cursor()

addNum = ("INSERT INTO UserInput (num) VALUES (%(x)s)") #sql command to insert x
X = {'x' : 57} # used a dic. incase we want to input multi. values

mycursor.execute(addNum, X)

key.commit()
mycursor.close()
key.close
