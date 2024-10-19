#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    sys.exit(f"usage: {os.path.basename(sys.argv[0])} FILE")

with open(sys.argv[1]) as file:
    for line in file:
        print(line.upper(), end='')
