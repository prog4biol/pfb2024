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

restriction_site_fwd = re.compile('([AG])(AATT[CT])')
restriction_site_rev = re.compile('([AG]AATT)([CT])')
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
    # The trick to this question is that the restriction enzyme binding
    # sequence is reverse-complement symmetric, but the cut-site is not:
    #    
    #    Fwd seq when the enzyme cuts the fwd strand: [AG]^AATT[CT]
    #    Fwd seq when the enzyme cuts the rev strand: [AT]AATT^[CT]
    #    
    # so, at every binding site, we have to cut both the forward and
    # reverse strands. If there are two or more binding sites, we have a
    # combinatorial problem. Implementing a stack-based algorithm can help
    # us solve this problem efficiently:


    # initialize an empty list for our cut fragments:
    fragment_list = []

    # initialize out stack with our starting sequence:
    sequence_stack = [sequence_records[sequence_name]]
    while sequence_stack:
        
        # create a sequence target for cutting on the forward strand:
        cut_target_fwd = sequence_stack.pop()
        # create a sequence target for cutting on the reverse strand:
        cut_target_rev = cut_target_fwd

        # perform the binding and cuts on both forward and reverse strands:
        cut_insert_fwd = restriction_site_fwd.sub(r'\1^\2',cut_target_fwd, count=1)
        cut_insert_rev = restriction_site_rev.sub(r'\1^\2',cut_target_rev, count=1)

        # split at cut site:
        cut_frags_fwd = cut_insert_fwd.split('^')
        cut_frags_rev = cut_insert_rev.split('^')

        # index 0 is the cut fragment, and has no more binding sites to cut;
        # because the cut-site is not symmetric, the lengths of the forward
        # and reverse fragments will differ in size:
        fragment_list.append(cut_frags_fwd[0])
        fragment_list.append(cut_frags_rev[0])

        # index 1 goes back into the stack to search for more binding sites
        # downstream; because the cut-site is not symmetric, the lengths of
        # the forward and reverse downstream sequences will differ in size:
        if len(cut_frags_fwd) > 1:
            sequence_stack.append(cut_frags_fwd[1])
        if len(cut_frags_rev) > 1:
            sequence_stack.append(cut_frags_rev[1])

    # The question prompt wants us to print the fragments in order like an
    # electrophoresis, which means longest to shortest. Call set() on
    # fragment_list to collapse redundant sequences:
    for i, sequence_fragment in enumerate(sorted(set(fragment_list), key=len, reverse=True)):
        fragment_length = len(sequence_fragment)
        print(f">{sequence_name}-frag{i+1} length={fragment_length}")
        print(sequence_fragment)
    
