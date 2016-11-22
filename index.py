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
        print("its in the Fast Brain ======> prime? " + str(FBsearch))
        FB.printFB() # print all fast brain values
    else:
        print("using the Slow Brain ======> prime? " + str(SB.SBPrimeDetermination(input)))
        if SB.SBPrimeDetermination(input) == True:
            FB.addit() # if it the slow brain says it's prime add it to the fast brain
        FB.printFB() # print all values

input = 199
brain(input)