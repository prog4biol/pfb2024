""" Tests for parse_fasta.py """

import os
from subprocess import getstatusoutput

PRG = './parse_fasta.py'
INPUT1 = './input1.fa'
INPUT2 = './input2.fa'

# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test1():
    """one record"""

    rv, out = getstatusoutput(f'{PRG} {INPUT1}')
    assert rv == 0
    assert out.strip() == "{'seq1': 'AACGA'}"


# --------------------------------------------------
def test2():
    """two records"""

    rv, out = getstatusoutput(f'{PRG} {INPUT2}')
    assert rv == 0
    assert out.strip() == "{'seq1': 'AACGATCCGAT', 'seq2': 'GGGTACCAAACGAT'}"
