#!/usr/bin/python

import sys
import random

def main():

    a = [0 for i in range(0,26)]

    for i in range(0,10000):
       chan = random.randint(0,23)
       if chan > 13:
           chan += 2
       a[chan] += 1

    print(a)

if __name__ == "__main__":
    main()
   

