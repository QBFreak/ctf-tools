#!/usr/bin/env python3

## binasc.py
## This script takes a file full of binary strings (bytes) seperated by
## whitespace and converts them into their ASCII values

import sys
import binascii

if not len(sys.argv) > 1:
    print("You need to specify an input file.")
    sys.exit()

# Determine the file from the command line
infile = sys.argv[1]

# Read the contents
fo = open(infile, "r")
contents = fo.read()
fo.close()

# Split the contents on whitespace into a list
words = contents.split()

for word in words:
    sys.stdout.write(chr(int(word, 2)))

print("")
