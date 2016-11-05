# Project Name: Prime-Time-Project
# File: Utility
# NOTE: this holds all the vital testing and maintenance functions

from Database import Database

# DATABASE TEST
# Test Key
user = 'root'
password = '1991'
host = 'localhost'
database = 'TEST_DB'

# Connection/Input/Print Test
print("TEST_START - Processing: Testing DB Connection/Input/Print...")
x = 0 # test input
mytestDB = Database(user, password, host, database) # using test key
mytestDB.connect() # Database Connection
#mytestDB.input(x) # inputing a value
#mytestDB.printAll() # printing all values
mytestDB.remove(x) # printing all values
mytestDB.printAll() # printing all values
print("TEST_END - Success: Connection/Input/Print test passed")
print("---------------------------------------------")
