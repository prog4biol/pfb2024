""" Tests for dna.py """

import os
import platform
from subprocess import getstatusoutput

PRG = './dna.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
TEST1 = ('./tests/inputs/input1.txt', '1 2 3 4')
TEST2 = ('./tests/inputs/input2.txt', '20 12 17 21')
TEST3 = ('./tests/inputs/input3.txt', '196 231 237 246')


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.exists(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    rv, out = getstatusoutput(f'{RUN}')
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_dies_no_args():
    """ Dies with no arguments """

    rv, out = getstatusoutput(RUN)
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_dies_too_many_args():
    """ Dies with too many arguments """

    rv, out = getstatusoutput(f'{RUN} foo bar baz')
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_arg():
    """ Uses command-line arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        dna = open(file).read()
        rv, out = getstatusoutput(f'{RUN} {dna}')
        assert rv == 0
        assert out == expected
