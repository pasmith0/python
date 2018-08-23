#!/usr/bin/python

import sys
from copy import deepcopy

def main():
    
    PoP_exid = [0x00,0x00,0x02]
    CP_exid  = [0xff,0x00,0xff]
    micsId   = [0x00,0x30,0x00]
    companyId = 0x01

    print(PoP_exid[0])
    print(PoP_exid[1])
    print(PoP_exid[2])

    print(CP_exid[0])
    print(CP_exid[1])
    print(CP_exid[2])


if __name__ == "__main__":
    main()
   

