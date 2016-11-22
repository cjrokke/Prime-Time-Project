from Database import Database
from Fast_Brain import FastBrain
from Slow_Brain import SlowBrain


user = 'root'
password = '1991'
host = 'localhost'
database = 'TEST_DB'


def brain(input):
    SB = SlowBrain()
    FB = FastBrain(user, password, host, database)
    FBsearch = FB.FBsearch(input) # run a fast brain search

    if FBsearch == True:
        FB.printFB() # print all fast brain values
    else:
        # if SB.SBPrimeDetermination(input) == True:
        #     FB.addit()
        # FB.printFB() # print all values

        SB.SBPrimeDetermination(input)
        FB.printFB() # print all values

input = 199
brain(input)