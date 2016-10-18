import mysql.connector
from mysql.connector import errorcode

try:
    cnn = mysql.connector.connect(
        user='root',
        password='1991',
        host='localhost',
        database='Prime-Time-Project' #this is the db name
    print ("Connected to Database!")

except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the username or password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    else:
        print(e)
cursor = cnn.cursor()
addNum =(I)


    )