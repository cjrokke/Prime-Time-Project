from Database import Database
import time


class FastBrain(object):
    def __init__(self, user, password, host, database):
        self.number = None
        self.FBtime = 0.00
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def FBsearch(self,d):
        self.number = d
        print("FAST_BRAIN SEARCH")
        FBdatabase = Database(self.user, self.password, self.host, self.database)
        start = time.time()
        result = FBdatabase.search(self.number)
        end = time.time()
        if result == True:
            self.FBtime = end - start
        print(" it took" , self.FBtime , )
        return result

    def addit(self):
        print("FAST_BRAIN ADD")
        FBdatabase = Database(self.user, self.password, self.host, self.database)
        FBdatabase.input(self.number)
        print("adding....")
        #FBdatabase.printAll()
        return True

    def printFB(self):
        print("FAST_BRAIN DATABASE PRINT")
        FBdatabase = Database(self.user, self.password, self.host, self.database)
        FBdatabase.connect()
        FBdatabase.printAll()
