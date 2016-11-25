from Database import Database
# import Fast_Brain
import math
import time

user = 'root'
password = '1991'
host = 'localhost'
database = 'TEST_DB'

class SlowBrain(object):
    def __init__(self):
        self.input = None
        self.genFlag = None
        self.divisors = []
        self.SBtime = 0.00

    def SBPrimeDetermination(self, d, f):
        self.input = d
        self.genFlag = f
        print'Starting up Slow Brain...'
        if(self.genFlag): self.exhaustiveAlg(self)  #Input from SNG
        else: self.fastAlg(self)    #Input form User

    def exhaustiveAlg(self):
        db = Database(user, password, host, database)
        start = time.time()
        #end = start   #used for logging faster SB times
        self.Divisors = []  # Divisor list
        z = 0.000000000000  # for testing divisors
        if (self.input == 2): return True  # 2 is Prime
        if (self.input == 3): return True  # 3 is Prime
        else:
            for i in range(1, (self.input / 2) + 1):
                for j in range(0, 2):               # test all divisors using nested for loops to prevent memory overflow for large inputs
                    if (i != self.input / 2 | j != 1):  # neglect last result, input will always be divisible by input and never by input-1
                        z = self.input % (2 * i + j)
                        if (z == 0 & (j == 1 | i == 1)):    #Only store odds > 2
                            #if (end == start): end = time.time()      #faster slow brain time logging
                            self.divisors.append(2 * i + j)  #NotPrime
            if (len(self.divisors) == 0):  # Prime!
                end = time.time()
                self.SBtime = end - start
                db.StorePrimeSBtime(self.input, self.SBtime)   #Prime!
                return True  # Prime!
            else:  # NotPrime
                #db.UpdateProb(self.divisors)
                for i in range(0, len(self.divisors)): print self.divisors[i]
                return False  # NotPrime

    def fastAlg(self):
        if (self.input <= 1):
            print'Invalid Format, please input a positive number > 1!'
            return False  # Anything less than 1 cannot be tested and thus is NotPrime by definition #
        if (self.input != int(self.input)):
            print'Invalid Format, please input an integer!'
            return False  # Non-integers cannot be tested and thus are NotPrime by definition
        if (self.input == 2): return True  # 2 is Prime
        if (self.input == 3): return True  # 3 is Prime
        else:  # the 3 primes and 2 conditions above cannot be accurately tested using the method below
            if (self.input % 2 == 0): return False  # even numbers = NotPrime
            else:  # Algorithm
                x = math.sqrt(self.input)  # Find the ranges max for checking prime
                if (x == int(x)): return False  # square root whole = NotPrime
                else:
                    x = int(x) + 1  # rounds square root to next whole number up
                    # print(x)
                    z = 0.000000000000  # Needs to be decimal so python doesn't round to zero
                    for i in range(2, x):
                        z = self.input % i
                        if (z == 0):  # If a number divides evenly
                            print'Your input was divisible by: ', self.input / i, ' and ', i
                            return False  # Not Prime
                        if (i + 1 == x): return True  #Has it checked against all numbers? → Prime

# testing
a = SlowBrain()
print("here" + str(a.SBPrimeDetermination(88, 1)))
