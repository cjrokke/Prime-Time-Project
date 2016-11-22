#DATABASE SCHEMA
#Database => TEST_DB
#Table => test_table
#Column=> a
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode


class Database(object):
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def connect(self):
        #this function will connect us to the db
        try:
            key = mysql.connector.connect(user = self.user, password = self.password , host = self.host, database = self.database)
            print ("  Success: Connected to Database")  # success
        except mysql.connector.Error as e:  # fail ... what's the issue?
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("  Something is wrong with the username or password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("  Database doesn't exist")
            else:
                print(e)
        return key

    def input (self, num):
        key = self.connect()

        mycursor = key.cursor()

        print ("  Processing: Inserting number into Database...")
        addNum = ("INSERT INTO test_table (a) VALUES (%(x)s)") #sql command to insert x
        X = {'x' : num} # used a dic. incase we want to input multi. values
        mycursor.execute(addNum, X)
        print ("  Success: Number inserted into Database")

        key.commit()
        mycursor.close()
        key.close()
        return

    def remove (self, num):
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: Deleting number from Database...")

        delNum = ("DELETE FROM test_table WHERE a = (%(x)s);") #sql command to insert x
        X = {'x' : num} # used a dic. incase we want to input multi. values
        mycursor.execute(delNum, X)

        print ("  Success: Number deleted from Database")

        key.commit()
        mycursor.close()
        key.close()

    def search (self, num):
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: searching for number (", num , ") in Database...")

        seaNum = ("SELECT a FROM test_table WHERE a = (%(x)s);") #sql command to insert x
        X = {'x' : num}
        mycursor.execute(seaNum, X)

        found = mycursor.fetchone()

        if found == None:
            print ("Not found")
        else:
            print("Found " + str(found[0]))

        print ("  Success: Number searched from Database")

        # mycursor.close()
        # key.close()

    def last (self): # Get the last prime number inputted into the database
                     # This will only work if we give each entry an order number
                     # In this case, column num increase by 1 for each input
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: searching for last input in Database...")

        seaNum = ("SELECT a FROM test_table ORDER BY num DESC LIMIT 1;") #sql command to insert x
        mycursor.execute(seaNum)

        found = mycursor.fetchone()

        print("Found " + str(found[0]))
        return int(found[0])

    def last2 (self): # Get the last number id inputted into the database
                     # This will only work if we give each entry an order number
                     # In this case, column num increase by 1 for each input
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: searching for last input in Database...")

        seaNum = ("SELECT num FROM test_table ORDER BY num DESC LIMIT 1;") #sql command to insert x
        mycursor.execute(seaNum)

        found = mycursor.fetchone()

        print("Found " + str(found[0]))
        return int(found[0])

    def find (self, num): #return prime for use in slow brain algorithm
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: searching for prime that order number is (", num , ") in Database...")

        seaNum = ("SELECT a FROM test_table WHERE num = (%(x)s);") #sql command to insert x
        X = {'x' : num}
        mycursor.execute(seaNum, X)

        found = mycursor.fetchone()

        if found == None:
            print ("Not found")
        else:
            print("Found " + str(found[0]))

        print ("  Success: Number searched from Database")
        return found
        # mycursor.close()
        # key.close()        
        
    def printAll (self):
        #to print all
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: Printing...")

        mycursor.execute("USE TEST_DB")  # select the database
        mycursor.execute("SELECT a from test_table")  # execute 'SHOW TABLES' (but data is not returned)

        for (test_table) in mycursor:
            print(str(test_table[0]), ", ", end="")

        print ("\n  Success: Printed")

        key.commit()
        mycursor.close()
        key.close()
        return

    def flush(self):
        key = self.connect()
        mycursor = key.cursor()

        print ("      Processing: Deleting all numbers from Database...")

        delNum = ("Truncate table test_table") #
        mycursor.execute(delNum)

        print ("      Success: Numbers deleted from Database")

        key.commit()
        mycursor.close()
        key.close()
