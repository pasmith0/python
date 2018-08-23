#!/usr/bin/python

import sys
from copy import deepcopy

def main():
    
    li = [ ('data_%d' % i) for i in range(10) ]
    print(li)

    di = { i: ('data_%d' % i) for i in range(10) }
    print(di)

    di2 = { ('data_%d' % i) : 0 for i in range(10) }
    di2['address'] = 12345678
    print(di2)

if __name__ == "__main__":
    main()
   

