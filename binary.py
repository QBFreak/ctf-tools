#!/usr/bin/env python3

## binary.py
## This script takes a file containing one or more binary strings and
## them into their ASCII values. Configurable start and stop bits, as well as
## byte length.

import sys

start = 0
byte = 8
stop = 1

if not len(sys.argv) > 1:
    print("You need to specify an input file.")
    sys.exit()

# Determine the file from the command line
infile = sys.argv[1]

# Read the contents
fo = open(infile, "r")
contents = fo.read()
fo.close()

words = []

# Drop any start and stop bits, chop up the rest into bytes
count = 0
word = ""
bits = list(contents)
for bit in bits:
    if bit != "1" and bit != "0":
        continue
    count += 1
    sys.stdout.write(bit)
    if count <= start and start > 0:
        sys.stdout.write(" ")
        continue
    elif count == start + byte - 1 + stop and stop > 0:
        sys.stdout.write(" ")
        continue
    elif count > start + byte - 1 + stop:
        sys.stdout.write(" ")
        count = 0
        words.append(word)
        word = ""
    else:
        word = word + bit

print(" ")

wordlist = []

# Reverse LSB/MSB
for word in words:
    word = word[::-1]
    wordlist.append(word)

words = wordlist

# Display the bytes in character form
for word in words:
    sys.stdout.write(chr(int(word, 2)))

print("")

# Display the bytes in decimal form
for word in words:
    sys.stdout.write(str(int(word, 2)))
    sys.stdout.write(" ")

print("")

# Display the bytes in hex form
for word in words:
    sys.stdout.write(hex(int(word, 2)))
    sys.stdout.write(" ")

print("")
