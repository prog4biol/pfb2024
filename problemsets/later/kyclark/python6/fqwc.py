#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    sys.exit(f"usage: {os.path.basename(sys.argv[0])} FILE")

num_lines, num_chars = 0, 0
with open(args[0]) as file:
    for line in file:
        num_lines += 1
        num_chars += len(line)

print(f"Num lines: {num_lines:,}")
print(f"Num chars: {num_chars:,}")
print(f"Avg line:  {int(num_chars/num_lines):,}")
