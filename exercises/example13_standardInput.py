#!/usr/bin/python
import sys

## Echoes stdin to stdout

line = sys.stdin.readline()
# Continues until EOF, which is an empty string
while line:
    print line,                    # Thru 2.7, the comma continues the print on the same line to avoid double newlines
    line = sys.stdin.readline()

sys.exit(0)
