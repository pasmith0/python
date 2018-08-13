#!/usr/bin/env python3

import pytest
import sys
import os
import time
import bits


def test_set_bit():
   v = 0x00
   v = bits.set_bit(v, 1)
   bits.pr(v)
   assert v == 0x02

   v = 0x06
   v = bits.set_bit(v, 0)
   bits.pr(v)
   assert v == 0x07


def test_clear_bit():
   v = 0x06
   v = bits.clear_bit(v, 1)
   bits.pr(v)
   assert v == 0x04

   v = 0x06
   v = bits.clear_bit(v, 0)
   bits.pr(v)
   assert v == 0x06

