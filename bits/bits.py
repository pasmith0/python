import pytest
import sys
import os
import time


def set_bit(v, bit):
   v |= (1 << bit)
   return v


def clear_bit(v, bit):
   v &= ~(1 << bit)
   return v

def is_bit_set(v, bit):
   return (v & (1<<bit)) != 0

def pr(v):
   print(v, "0b" '{:b}'.format(v), "0x" '{:x}'.format(v))



