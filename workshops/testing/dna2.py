#!/usr/bin/env python3
"""
A program to report the frequency of DNA nucleotides
This version introduces the main() function
"""

import sys
import os

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        sys.exit("usage: {} DNA".format(os.path.basename(sys.argv[0])))

    dna = args[0]
    count_a, count_c, count_g, count_t = 0, 0, 0, 0

    for base in dna:
        if base == 'A':
            count_a += 1
        elif base == 'C':
            count_c += 1
        elif base == 'G':
            count_g += 1
        elif base == 'T':
            count_t += 1

    print(count_a, count_c, count_g, count_t)

# --------------------------------------------------
if __name__ == '__main__':
    main()
