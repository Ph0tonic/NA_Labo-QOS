'''
Labo n°3 - Réseau et application
Bulloni Lucas & Wermeille Bastien
Python version: 3.5
'''
import random
from collections import deque
import time

class TokenBucket(object):

    def __init__(self, burstLimit):
        self.burstLimit = burstLimit
        self.messages = deque([])

    def enqueue(self, message):
        if len(self.messages) == self.burstLimit:
            return None
        else:
            self.messages.append(message)
            return message

    def dequeue(self):
        try:
            val = self.messages.pop()
        except IndexError:
            val = None

        return val

    def printSize(self):
        print(str(len(self.messages)) + '/' + str(self.burstLimit) + ' messages')

if __name__ == '__main__':
    bucket = TokenBucket(10)

    while True:
        qorDeQ = random.random()

        if qorDeQ > 0.2 :
            val = bucket.enqueue(random.randint(0,100))
            print('queue message')

            if val != None:
                bucket.printSize()
            else:
                print('bucket is full')

        else :
            print('dequeue message')
            val = bucket.dequeue()

            if val == None:
                print('Bucket is empty')
            else:
                bucket.printSize()

        time.sleep(0.5)
