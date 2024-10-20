#!/usr/bin/env python3
# 7. Determine the site(s) of the physical cut(s) by ApoI in the above sequence. Print out the sequence with "^" at the cut site.
# Hints:
# Use sub()
# 
# Use subpatterns (parentheses and group() ) to find the cut site within the pattern.
# Example: if the pattern is GACGT^CT the following sequence
#    AAAAAAAAGACGTCTTTTTTTAAAAAAAAGACGTCTTTTTTT
# we want to display the cut site like this:
#
#    AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT

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
    sequence_string = sequence_records[sequence_name]
    
    sequence_string = restriction_site.sub(r'\1^\2', sequence_string)
    sequence_strings[1] = sequence_string[::-1].translate(_NUCLEOTIDE_COMPLEMENT)
        
    # here sequence_strings[0] contains no carats and sequence_strings[1] contains
    # our sequence with carats:
    print(f">{sequence_name}")
    print(sequence_strings[1])

    
