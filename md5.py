#!/usr/bin/python

import hashlib
import sys

if len(sys.argv) == 1:
    print("Please specify a string to hash")
    exit()

text = sys.argv[1]

sys.stdout.write(hashlib.md5(text).hexdigest())
print("  {}".format(text))
