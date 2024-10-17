#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2024-10-17
Purpose: FASTA parser
"""

import argparse
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    return Args(file=args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    rec_id = ''
    seq = []
    records = {}
    for line in map(str.rstrip, args.file):
        if line.startswith('>'):
            if rec_id:
                records[rec_id] = ''.join(seq)

            rec_id = line[1:]
            seq = []
        else:
            seq.append(line)

    if rec_id:
        records[rec_id] = ''.join(seq)

    print(records)


# --------------------------------------------------
if __name__ == '__main__':
    main()
