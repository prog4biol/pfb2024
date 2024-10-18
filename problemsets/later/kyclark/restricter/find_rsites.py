#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2024-10-17
Purpose: Rock the Casbah
"""

import argparse
import re
from Bio import SeqIO
from typing import NamedTuple, TextIO

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
    site: str
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--site',
                        help='Restriction site',
                        metavar='STR',
                        required=True)

    parser.add_argument('-f',
                        '--file',
                        help='FASTA file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    args = parser.parse_args()

    return Args(site=args.site, file=args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    parser = SeqIO.parse(args.file, 'fasta')
    site = ''.join(map(lambda c: IUPAC.get(c, c), list(args.site)))
    if '^' in site:
        parts = site.split('^')
        site = f'({parts[0]})({parts[1]})'

    for rec in parser:
        seq = str(rec.seq)
        new = re.sub(site, r'\1^\2', seq)
        print(new)


# --------------------------------------------------
if __name__ == '__main__':
    main()
