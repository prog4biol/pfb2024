#!/usr/bin/env python3
"""
A program to report the frequency of DNA nucleotides
This count() function uses collections.Counter
"""

import argparse
from collections import Counter

# --------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Count DNA bases')
    parser.add_argument('dna')
    args = parser.parse_args()
    count_a, count_c, count_g, count_t = count(args.dna)

    print(count_a, count_c, count_g, count_t)


# --------------------------------------------------
def count(dna):
    """ Count bases in DNA """

    counts = Counter(dna)
    return (counts.get('A', 0), counts.get('C', 0), counts.get('G', 0),
          counts.get('T', 0))


# --------------------------------------------------
def test_count():
    """ Test count """

    assert count('') == (0, 0, 0, 0)
    assert count('123XYZ') == (0, 0, 0, 0)
    assert count('A') == (1, 0, 0, 0)
    assert count('C') == (0, 1, 0, 0)
    assert count('G') == (0, 0, 1, 0)
    assert count('T') == (0, 0, 0, 1)
    assert count('ACCGGGTTTT') == (1, 2, 3, 4)


# --------------------------------------------------
if __name__ == '__main__':
    main()
