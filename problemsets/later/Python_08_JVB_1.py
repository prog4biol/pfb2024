#!/usr/bin/env python3

import sys

sequence_filename = sys.argv[1]
sequence_file = open(sequence_filename, 'r')

sequence_name = None
sequence_comp = {}
for line in sequence_file:
    # leading and trailing whitespace in FASTA files is
    # meaningless, just remove it.
    line = line.strip()

    # if the lines begins with '>', it starts a (new)
    # FASTA record, but the first FASTA record '>'
    # we encounter we have no sequence, so we have to
    # defer until we get to the next sequence:
    if line.startswith('>'):
        # line[1:] removes '>', then we split and take
        # only the first element (the sequence name):
        sequence_name = line[1:].split(maxsplit=1)[0]
        sequence_comp[sequence_name] = {'A':0, 'T':0, 'C':0, 'G':0}
    else:
        # normalize all nucleotides to upper-case so
        # we can count accurately:
        for nt in line.upper():
            sequence_comp[sequence_name][nt] += 1

print("seqName\tA_count\tT_count\tG_count\C_count")
for sequence_name in sequence_comp:
    # Using end='' kwarg to print(), we can print a single
    # column value.
    print(sequence_name, end='')
    for nt in ('A','T','G','C'):
        print("\t{0:d}".format(sequence_comp[sequence_name][nt]), end='')

    # now add the '\n' at the end of the line:
    print('')  
