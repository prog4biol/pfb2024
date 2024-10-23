#!/usr/bin/env python3
"""
A program to report the frequency of DNA nucleotides
"""

import argparse

parser = argparse.ArgumentParser(description='Count DNA bases')
parser.add_argument('dna')
args = parser.parse_args()
count_a, count_c, count_g, count_t = 0, 0, 0, 0

for base in args.dna:
    if base == 'A':
        count_a += 1
    elif base == 'C':
        count_c += 1
    elif base == 'G':
        count_g += 1
    elif base == 'T':
        count_t += 1

print(count_a, count_c, count_g, count_t)
