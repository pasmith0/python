#!/usr/bin/python

import sys
import bits

def main():
    
    #for arg in sys.argv[1:]:
    #    print arg

    if len(sys.argv) < 3:
        print("Usage: %s val bit" % sys.argv[0])
        return

    try:
        v = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError as verr:
        print("Please enter an integer for val and bit")
        return

    bits.pr(v)
    for bit in range(8) :
        print( " bit %d of %d is %s" % (bit, v, bits.is_bit_set(v, bit)) )

    print("Before")
    bits.pr(v)
    s = bits.set_bit(v, b)
    print("After setting bit %d" % b)
    bits.pr(s)
    c = bits.clear_bit(v, b)
    print("After clearing bit %d" % b)
    bits.pr(c)

if __name__ == "__main__":
    main()
    

