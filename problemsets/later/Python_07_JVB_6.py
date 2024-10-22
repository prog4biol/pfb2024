#!/usr/bin/env python3
# 6. The enzyme ApoI has a restriction site: R^AATTY where R and Y are
#    degenerate nucleotides. See the IUPAC table to identify the nucleotide
#    possibilities for the R and Y. Write a regular expression to find
#    and print all occurrences of the site in the following sequence
#    Python_07_ApoI.fasta.

import re
import sys

_NUCLEOTIDE_COMPLEMENT = {
    65: 'T',  97: 't',
    66: 'V',  98: 'v',
    67: 'G',  99: 'g',
    68: 'H', 100: 'h',
    71: 'C', 103: 'c',
    72: 'D', 104: 'd',
    75: 'M', 107: 'm',
    77: 'K', 109: 'k',
    78: 'N', 110: 'n',
    82: 'Y', 114: 'y',
    83: 'W', 115: 'w',
    84: 'A', 116: 'a',
    85: 'A', 117: 'a',
    86: 'B', 118: 'b',
    87: 'S', 119: 's',
    89: 'R', 121: 'r',
}

input_filename = sys.argv[1]

input_file = open(input_filename, 'r')

restriction_site = re.compile('([AG])(AATT[CT])')
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
    sequence_strings = (
        sequence_records[sequence_name],
        sequence_records[sequence_name][::-1].translate(_NUCLEOTIDE_COMPLEMENT)
    )

    sequence_count = 0
    for sequence_string in sequence_strings:
        strand = '-' if sequence_count else '+'
        
        print(f">{sequence_name} strand=[{strand}]")
        for match in restriction_site.finditer(sequence_string):
            print(match.group(1) + '^' + match.group(2))
        sequence_count += 1
            

    
    

