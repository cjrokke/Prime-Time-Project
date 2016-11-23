from Database import Database


class FastBrain(object):
    def __init__(self, user, password, host, database):
        self.number = None
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def FBsearch(self,d):
        self.number = d
        print("FAST_BRAIN SEARCH")
        FBdatabase = Database(self.user, self.password, self.host, self.database)
        FBdatabase.connect()
        return FBdatabase.search(self.number)

    def addit(self):
        print("FAST_BRAIN ADD")
        FBdatabase = Database(self.user, self.password, self.host, self.database)
        FBdatabase.connect()
        FBdatabase.input(self.number)
        print("adding....")
        #FBdatabase.printAll()
        return True
    def printFB(self):
        print("FAST_BRAIN DATABASE PRINT")
        FBdatabase = Database(self.user, self.password, self.host, self.database)
        FBdatabase.connect()
        FBdatabase.printAll()
