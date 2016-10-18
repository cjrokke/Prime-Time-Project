import mysql.connector
from mysql.connector import errorcode

try:
    key = mysql.connector.connect(
        user='root',
        password='1991', #my connection password
        host='localhost',
        database='Prime-Time-Project' #this is the db name
    )
    print ("Connected to Database!")

except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the username or password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    else:
        print(e)
cursor = key.cursor()
addName =("INSERT INTO Name (fName, lName) VALUES (%s, %s)")
fName="Vehans"
lName="Ayvazi"

empName=(fName, lName)

cursor.execute(addName, empName)

key.commit()
cursor.close()
key.close
