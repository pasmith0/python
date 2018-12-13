#!/usr/bin/env python3
import pytest
import sys
import os
import time
import json

if len(sys.argv) < 2:
    print("Usage: %s filename" % sys.argv[0])
    sys.exit(1)
    
for i in range(1,len(sys.argv)):
    with open(sys.argv[i]) as f:
        print("--- " + sys.argv[i] + " ---")
        file_dat = f.read()
        print(file_dat)

