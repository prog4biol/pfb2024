#!/usr/bin/env python3
# Now that you've done your restriction digest, determine the lengths of your fragments
# and sort them by length (in the same order they would separate on an electrophoresis gel).
# Hint: Convert this string:
#
# AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT
# Into this list:
#
# ["AAAAAAAAGACGT","CTTTTTTTAAAAAAAAGACGT","CTTTTTTT"]

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


fragment_list = []
for sequence_name in sequence_records:
    sequence_string = sequence_records[sequence_name]
    
    sequence_string = restriction_site.sub(r'\1^\2', sequence_string)

    # can append() multiple items to a list using extend():
    fragment_list.extend(sequence_string.split('^'))

    # The question prompt wants us to print the fragments in order like an
    # electrophoresis, which means longest to shortest. Call set() on
    # fragment_list to collapse redundant sequences:
    for i, sequence_fragment in enumerate(sorted(set(fragment_list), key=len, reverse=True)):
        fragment_length = len(sequence_fragment)
        print(f">{sequence_name}-frag{i+1} length={fragment_length}")
        print(sequence_fragment)
    
