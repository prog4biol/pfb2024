#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) not in [1, 2]:
    sys.exit(f"usage: {os.path.basename(sys.argv[0])} FILE [OUTFILE]")

out = open(args[1], 'wt') if len(args) == 2 else sys.stdout
with open(args[0]) as file:
    for line in file:
        print(line.upper(), end='', file=out)
