#!/usr/bin/env python3

import re
import sys

input_filename = sys.argv[1]

input_file = open(input_filename, 'r')

fasta_header = re.compile(r'^>(\S+)\ ?(.*)?')

sequence_name = ''
sequence_records = {}
for line in input_file:
    line = line.strip()
    
    match = fasta_header.match(line)
    if match:
        sequence_name = match.group(1)
        sequence_records[sequence_name] = ''
    else:
        sequence_records[sequence_name] += line

for sequence_name in sequence_records:
    sequence_string = sequence_records[sequence_name]
    print(f"{sequence_name}\t{sequence_string}")

