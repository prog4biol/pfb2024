#!/usr/bin/env python3
# 3. Using pattern matching, find all the FASTA header lines in
#    Python_07.fasta. Note that the format for a header in a
#    FASTA file is a line that starts with a greater than symbol
#    and is followed by some text (e.g. >seqName description where
#    seqName is the sequence name or identifier. The identifier
#    cannot have spaces in it. The description that follows it can
#    have spaces.)

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

