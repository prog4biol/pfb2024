#!/usr/bin/env python3
# 4. If a line matches the format of a FASTA header, extract the
#    sequence name and description using sub patterns (groups).
# 
#    Print sequence information in this format:
#        id:seqName desc:seqDescription

import re
import sys

input_filename = sys.argv[1]

input_file = open(input_filename, 'r')

fasta_header = re.compile(r'^>(\S+)\ ?(.*)?')

for line in input_file:
    match = fasta_header.match(line)
    if match:
        print(f'id:{match.group(1)} desc:{match.group(2)}')

