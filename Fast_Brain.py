from Database import Database


class FastBrain(object):
    def __init__(self, user, password, host, database):
        self.number = None
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def FBPrimeDetermination(self,d):
        self.number = d
        FBdatabase = Database(self.user, self.password, self.host, self.database)
        FBdatabase.connect()
        if FBdatabase.search(self.number) == True:
            FBdatabase.input(self.number)
            return False
        return True
