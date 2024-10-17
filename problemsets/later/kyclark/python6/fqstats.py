#!/usr/bin/env python3

import os
import sys
from collections import Counter
from typing import Dict

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        sys.exit(f"usage: {os.path.basename(sys.argv[0])} FILE")

    msg = '{}: A {} C {} G {} T {} GC {:2.02f}'
    with open(args[0]) as file:
        for line in map(str.strip, file):
            vals = line.split()
            if len(vals) == 2:
                counts = Counter(vals[1].upper())
                print(msg.format(vals[0],
                                 counts.get('A', 0),
                                 counts.get('C', 0),
                                 counts.get('G', 0),
                                 counts.get('T', 0),
                                 gc(counts)))


# --------------------------------------------------
def gc(freq: Dict[str, int]) -> float:
    total = sum(freq.values())
    return (100 * (freq.get('G', 0) + freq.get('C', 0))) / total \
        if total > 0 else 0.


# --------------------------------------------------
if __name__ == '__main__':
    main()
