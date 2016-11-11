from Database import Database
from Fast_Brain import FastBrain
from Slow_Brain import SlowBrain


user = 'root'
password = '1991'
host = 'localhost'
database = 'TEST_DB'

FB = FastBrain(user, password, host, database)
print(FB.FBPrimeDetermination(6))
