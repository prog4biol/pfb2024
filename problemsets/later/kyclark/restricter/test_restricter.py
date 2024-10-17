""" Tests for parse_fasta.py """

import os
from subprocess import getstatusoutput

PRG = './find_rsites.py'
INPUT1 = './tests/inputs/input1.fa'
INPUT2 = './tests/inputs/input2.fa'
APOL_OUT = './tests/expected/apol.txt'

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
    """test"""

    rv, out = getstatusoutput(f'{PRG} -s "GACGT^CT" -f {INPUT1}')
    assert rv == 0
    assert out.strip() == "AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT"


# --------------------------------------------------
def test_apol():
    """apol"""

    rv, out = getstatusoutput(f'{PRG} -s "R^AATTY" -f {INPUT2}')
    assert rv == 0
    expected = open(APOL_OUT).read().rstrip()
    assert out.strip() == expected
