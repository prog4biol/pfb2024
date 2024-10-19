#!/usr/bin/env python3

import re
import sys

input_filename = sys.argv[1]

input_file = open(input_filename, 'r')

fasta_header = re.compile(r'^>(\S+)\ ?(.*)?')

for line in input_file:
    match = fasta_header.match(line)
    if match:
        print(f'id:{match.group(1)} desc:{match.group(2)}')

