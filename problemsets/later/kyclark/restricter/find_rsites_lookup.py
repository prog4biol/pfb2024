#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2024-10-17
Purpose: Rock the Casbah
"""

import argparse
import re
import sys
from collections import defaultdict
from Bio import SeqIO
from typing import Dict, List, NamedTuple, TextIO

IUPAC = {
    'R': '[AG]',
    'Y': '[CT]',
    'S': '[GC]',
    'W': '[AT]',
    'K': '[GT]',
    'M': '[AC]',
    'B': '[CGT]',
    'D': '[AGT]',
    'H': '[ACT]',
    'V': '[ACG]',
    'N': '.',
}


class Args(NamedTuple):
    """ Command-line arguments """
    enzyme: str
    file: TextIO
    lookup: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-e',
                        '--enzyme',
                        help='Enzyme name',
                        metavar='ENZYME',
                        required=True)

    parser.add_argument('-f',
                        '--file',
                        help='FASTA file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-l',
                        '--lookup',
                        help='Enzyme lookup file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    args = parser.parse_args()

    return Args(enzyme=args.enzyme, file=args.file, lookup=args.lookup)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    lookup = get_lookup(args.lookup)
    sites = lookup.get(args.enzyme)
    if len(sites) == 0:
        sys.exit(f"Unknown enzyme '{args.enzyme}'")

    parser = SeqIO.parse(args.file, 'fasta')
    for rec in parser:
        seq = str(rec.seq)
        for site in sites:
            site = ''.join(map(lambda c: IUPAC.get(c, c), list(site)))
            if '^' in site:
                parts = site.split('^')
                pattern = f'({parts[0]})({parts[1]})'
                new = re.sub(pattern, r'\1^\2', seq)
                if new != seq:
                    print(new)


# --------------------------------------------------
def get_lookup(file: TextIO) -> Dict[str, List[str]]:
    """ Get lookup """

    # skip 10 header lines
    for _ in range(10):
        _ = file.readline()

    lookup = defaultdict(list)
    pattern = re.compile(r'^(.+)\s{2,}(\S+)')
    for line in map(str.rstrip, file):
        if match := pattern.search(line):
            name = match.group(1).strip()
            site = match.group(2).strip()
            lookup[name].append(site)

    return lookup


# --------------------------------------------------
if __name__ == '__main__':
    main()
