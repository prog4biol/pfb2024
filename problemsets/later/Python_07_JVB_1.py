#!/usr/bin/env python3

import re
import sys

input_filename = sys.argv[1]

input_file = open(input_filename, 'r')

# since our pattern never changes, compile it for use up-front:
pattern = re.compile(r'Nobody', flags=re.IGNORECASE)

# BONUS: To tell the user which line we are on, we need to
# initialize a variable *above* the loop so that we can
# increment it each iteration:
line_number = 0
for line in input_file:
    # By incrementing our line_number variable *before* we print
    # its value, we ensure a 1-based count (first line is line 1)
    line_number += 1
    for occurance in pattern.finditer(line):
        # let's assume we want 1-based positions:
        print(f'{occurance.group()} at line {line_number}, position {occurance.start()+1}')

# nice and tidy:
input_file.close()
