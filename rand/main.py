#!/usr/bin/python

from __future__ import print_function
import sys
import random

class PrgmConst:
    prgmFreq = None
    responseCode = 0
    prgmPassRecovPW = None


def main():
    
   factoryFreqs=[2,3,4,6,8,10,12,14,16,18,20,22,24,26,28,30,35,40,45,
                  50,55,60,65,70,75,80,85,90,95,100,110,120,130,140,
                  150,160,170,180,190,200,225,250,275,300,325,350,375,
                  400,500,600,700,800,900,1000,1100,1200,1300,1400,
                  1500,1600,1700,1800,1900,2000]

   factoryPrgmPassiveRecoveryPW=[
           1,2,3,1,2,3,1,2,3,1,
           2,3,1,2,3,1,2,3,1,2,
           3,1,2,3,1,2,3,1,2,3,
           1,2,3,1,2,3,1,2,3,1,
           2,3,1,2,3,1,2,3,1,2,
           3,1,2,3,1,2,3,1,2,3,
           1,2,3,1]

   initialPgrmConst = PrgmConst()
   initialPgrmConst.prgmFreq = []
   initialPgrmConst.prgmFreq = factoryFreqs 
   initialPgrmConst.responseCode = 0xff
   initialPgrmConst.prgmPassRecovPW = []
   initialPgrmConst.prgmPassRecovPW = factoryPrgmPassiveRecoveryPW

   randPrgmConst = initialPgrmConst
   randomFreqs = random.sample(range(2,2000),len(initialPgrmConst.prgmFreq))
   randomFreqs.sort()
   randPrgmConst.prgmFreq = randomFreqs

   print( "randPrgmConst.prgmFreq: ", end='' )
   print( randPrgmConst.prgmFreq )
   print( "randPrgmConst.pgrmPassRecovPW: ", end='' )
   print( randPrgmConst.prgmPassRecovPW )
   print( "randPrgmConst.responseCode: ", end='' )
   print( randPrgmConst.responseCode )
  

if __name__ == "__main__":
    main()
    

