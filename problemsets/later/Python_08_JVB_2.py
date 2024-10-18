#!/usr/bin/env python3

import sys

sequence_filename = sys.argv[1]
sequence_file = open(sequence_filename, 'r')

sequence_name = None
sequence_string = {}
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
        sequence_string[sequence_name] = ''
    else:
        # normalize all nucleotides to upper-case so
        # we can count accurately:
        sequence_string[sequence_name] += line.upper()

        
for sequence_name in sequence_string:
    # Using end='' kwarg to print(), we can print a single
    # column value.
    print(f"{sequence_name}-frame-1-codons")
    sep=''
    for i in range(0, len(sequence_string[sequence_name]), 3):
        codon = sequence_string[sequence_name][i:i+3]

        # The sequence lengths may not be all be in multiples
        # of three, so omit last bit if sequence < 3 nt long:
        if len(codon) == 3:
            print("{sep:s}{seq:s}".format(sep=sep, seq=codon), end='')
        sep=' '

    # now add the '\n' at the end of the line:
    print('')  
