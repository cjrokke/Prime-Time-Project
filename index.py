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

    if FB.FBsearch(input) == True:
        print("its in the FB ======> prime? " + str(FB.FBsearch(input)))
        FB.printFB()
    else:
        print("using the SB ======> prime? " + str(SB.SBPrimeDetermination(input)))
        if SB.SBPrimeDetermination(input) == True:
            FB.addit()
        FB.printFB()



input = 17
brain(input)