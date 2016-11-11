from Database import Database
#import Fast_Brain
import math

class SlowBrain(object):
    def __init__(self):
        self.number = None

    def primeDetermination(self, d):
        self.number = d
        if self.number % 2 == 0: # Is the number even?
            #print ("not prime (its even)")
            return False
        else:
            x = math.sqrt(self.number) # Find the ranges max for checking prime
            x = int(x) # rounds number down
            z = 0.0 # Needs to be decimal so python doesn't round to zero
            for i in range(3, x):
                z = self.number % i
                if z == 0: # If a number divides evenly
                    #print ("not prime")
                    return False # Not Prime
                if i + 1 == x: # Has it checked against all number?
                    #print ("prime")
                    return True # Prime






#testing
#a = SlowBrain()
#print(a.primeDetermination(13))
#a.primeDetermination(13)