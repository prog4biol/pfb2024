#!/usr/bin/env python3

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

sequence_filename = sys.argv[1]
sequence_file = open(sequence_filename, 'r')

sequence_name = None
sequence_records = {}
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
        sequence_records[sequence_name] = ''
    else:
        # normalize all nucleotides to upper-case so
        # we can count accurately:
        sequence_records[sequence_name] += line.upper()


for sequence_name in sequence_records:
    # To avoid having to duplicate the loops to compute codons
    # twice (once for forward orientation and second for the
    # reverse complemented orientation), create a 2-tuple of
    # sequence_strings (forward and rev-comp'd):
    sequence_strings = (
        sequence_records[sequence_name],
        sequence_records[sequence_name][::-1].translate(_NUCLEOTIDE_COMPLEMENT)
    )
    frame = 0
    for sequence_string in sequence_strings:
        # To output three frames, that's three loops, each with
        # coordinate offset of `offset`
        for offset in range(3):
            print(f"{sequence_name}-frame-{frame+1}-codons")
            sep=''
            for i in range(0, len(sequence_string), 3):
                codon = sequence_string[offset+i:offset+i+3]
                
                # The sequence lengths may not be all be in multiples
                # of three, so omit last bit if sequence < 3 nt long:
                if len(codon) == 3:
                    print("{sep:s}{seq:s}".format(sep=sep, seq=codon), end='')
                    sep=' '

            # now add the '\n' at the end of the line:
            print('')
            frame += 1
