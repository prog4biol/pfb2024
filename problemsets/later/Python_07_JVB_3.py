#!/usr/bin/env python3

import re
import sys

input_filename = sys.argv[1]

input_file = open(input_filename, 'r')

# since our pattern never changes, compile it for use up-front:
fasta_header = re.compile(r'^>')

for line in input_file:
    # Remove '\n' at the end if we plan on printing it:
    line = line.rstrip()
    
    match = fasta_header.match(line)
    if match:
        print(line)

