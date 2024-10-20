#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2024-10-19
Purpose: DNA stuff
"""

import math
from collections import Counter
from typing import Dict, NamedTuple


class DNA(NamedTuple):
    """DNA"""

    seq: str
    name: str
    org: str


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    dna1 = DNA(seq="AACGAT", name="Seq1", org="Hooman")
    dna2 = DNA(seq="GGAGGTA", name="Seq2", org="Doge")

    for rec in [dna1, dna2]:
        print(">>>")
        print(rec)
        print(f"Seq  : {rec.seq}")
        print(f"Name : {rec.name}")
        print(f"Org  : {rec.org}")
        print(f"GC   : {gc(rec.seq):0.02f}")
        print(f"Len  : {seq_len(rec.seq)}")
        print(f"FASTA:\n{to_fasta(rec)}")


# --------------------------------------------------
def seq_len(seq: str) -> float:
    """Return sequence length"""

    return len(seq)


# --------------------------------------------------
def test_seq_len() -> None:
    """Test seq_len"""

    assert seq_len("") == 0
    assert seq_len("A") == 1
    assert seq_len("AA") == 2
    assert seq_len("ACCGGGTTTT") == 10


# --------------------------------------------------
def comp(seq: str) -> Dict[str, int]:
    """Return sequence composition"""

    return dict(Counter(seq))


# --------------------------------------------------
def test_comp() -> None:
    """Test comp"""

    assert comp("") == {}
    assert comp("A") == {"A": 1}
    assert comp("AA") == {"A": 2}
    assert comp("ACCGGGTTTT") == {"A": 1, "C": 2, "G": 3, "T": 4}


# --------------------------------------------------
def gc(seq: str) -> float:
    """Calculate GC content"""

    n = len(seq)
    if n == 0:
        return 0.0

    seq = seq.upper()
    return (seq.count("G") + seq.count("C")) / n


# --------------------------------------------------
def test_gc() -> None:
    """Test gc"""

    assert gc("") == 0.0
    assert gc("A") == 0.0
    assert gc("T") == 0.0
    assert gc("G") == 1.0
    assert gc("C") == 1.0
    assert gc("ACGT") == 0.5
    assert math.isclose(gc("GGAGGTA"), 0.57, rel_tol=0.01)
    assert math.isclose(gc("AACGAT"), 0.33, rel_tol=0.01)


# --------------------------------------------------
def to_fasta(rec: DNA) -> str:
    """DNA to FASTA"""

    return f">{rec.name} {rec.org}\n{rec.seq}\n"


# --------------------------------------------------
def test_to_fasta() -> None:
    """Test to_fasta"""

    dna1 = DNA(seq="AACGAT", name="Seq1", org="Hooman")
    assert to_fasta(dna1) == ">Seq1 Hooman\nAACGAT\n"

    dna2 = DNA(seq="GGAGGTA", name="Seq2", org="Doge")
    assert to_fasta(dna2) == ">Seq2 Doge\nGGAGGTA\n"


# --------------------------------------------------
def is_same(rec1: DNA, rec2: DNA) -> bool:
    """ Compare DNA records for samename """

    return rec1.name == rec2.name and \
        rec1.org == rec2.org and \
        rec1.seq == rec2.seq


# --------------------------------------------------
def test_is_same() -> None:
    """Test is_same"""

    dna1 = DNA(seq="AACGAT", name="Seq1", org="Hooman")
    dna2 = DNA(seq="AACGAT", name="Seq1", org="Hooman")
    assert is_same(dna1, dna2)

    dna3 = DNA(seq="GGAGGTA", name="Seq2", org="Doge")
    assert not is_same(dna1, dna3)


# --------------------------------------------------
if __name__ == "__main__":
    main()
