#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    sys.exit(f"usage: {os.path.basename(sys.argv[0])} FILE")

trans = str.maketrans({
    'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A',
    'a': 't', 'c': 'g', 'g': 'c', 't': 'a'
})

with open(args[0]) as file:
    for line in map(str.strip, file):
        vals = line.split()
        if len(vals) == 2:
            rc = ''.join(reversed(vals[1].translate(trans)))
            print(f'>{vals[0]}\n{rc}')
