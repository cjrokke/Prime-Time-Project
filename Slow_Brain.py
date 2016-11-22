from Database import Database
#import Fast_Brain
import math

def prime(number): ## user input
    if number % 2 == 0: #Is the number even?
        return False
    else:
        x = math.sqrt(number) #Find the ranges max for checking prime
        x = int(x)+1 #rounds number down
        z = 0.0 #Needs to be decimal so python doesn't round to zero
        for i in range(3, x):
            z = number % i
            if z == 0: #If a number divides evenly 
                return False #Not Prime
            if i + 1 == x: #Has it checked against all number?
                return True #Prime

def prime2(number): #SNG input
    if number % 2 == 0: #Is the number even?
        return False
    else:
        myDB = Database("Mike","1234","localhost","test_db")
        myDB.connect()
        x = math.sqrt(number) #Find the ranges max for checking prime
        x = int(x)+1 #rounds number down
        y = myDB.last()
        print(x)
        print(y)
        z = 0.0 #Needs to be decimal so python doesn't round to zero
        for i in range(3, y):
            z = number % i
            if z == 0: #If a number divides evenly 
                return False #Not Prime
            if i + 1 == x: #Has it checked against all number?
                return True #Prime

##print(prime(17))
myDB = Database("Mike","1234","localhost","test_db")
