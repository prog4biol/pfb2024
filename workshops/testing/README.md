# Introduction to Testing with Python

We will use [Pytest](https://docs.pytest.org/en/stable/) to run two types of tests:

1. Integration tests: Runs the program on the command-line with arguments and ensures the program as a whole works correctly and fails gracefully.
2. Unit tests: Runs individual functions

This directory contains six Python programs that all pass the integration tests.
Testing allows you the freedom to _refactor_ your code.
Once you have a working program that passes your tests, you can rewrite your code to make it cleaner or shorter or faster or try some other approach and run your tests to ensure it still works.

## The Program

We will use the Rosalind [DNA](https://rosalind.info/problems/dna/) challenge.
We will write a Python program called _dna.py_.
When given no arguments, it should print a "usage" statement:

```
$ ./dna.py
usage: dna.py DNA
```

When given string (that we hope is DNA), it should print the number of As, Cs, Ts, and Gs separated by spaces:

```
$ ./dna.py ACCGGGTTTT
1 2 3 4
```

The string might be empty:

```
$ ./dna.py ""
0 0 0 0
```

Here is a more realistic example:

```
$ ./dna.py AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
20 12 17 21
```

## Integration Tests

An integration test will use Python to run the program on the command line as the user will do and ensure that the program works correctly and fails gracefully.
It's common to put tests into a _tests_ directory, which is where I will place a Python module for testing along with a few input files:

```
$ tree tests
tests
├── dna_test.py
└── inputs
    ├── input1.txt
    ├── input2.txt
    └── input3.txt

2 directories, 4 files
```

NOTE: The file _tests/dna_test.py_ follows a Pytest convention of adding "_test" to the filename to indicate that Pytest should look for tests in this file. It's not a requirement to name the file this way. You can always specify the test file for Pytest.

The test file begins with a docstring for the module (this is not an executable script) along with some imports

```
""" Tests for dna.py """

import os
import platform
from subprocess import getstatusoutput
```

* The `os` module is for interacting with the operating system.
* The `platform` module will tell me if the tests are running on Windows
* The `subprocess` module provides the `getstatusoutput` function for running an external process

Next are some "constant" definitions for the name of the program I'm testing, how I need to execute the program, and some test input files along with the expected results:

```
PRG = './dna.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
TEST1 = ('./tests/inputs/input1.txt', '1 2 3 4')
TEST2 = ('./tests/inputs/input2.txt', '20 12 17 21')
TEST3 = ('./tests/inputs/input3.txt', '196 231 237 246')
```

Pytest will execute the tests in the order they are defined in the file.
The first test checks if the _dna.py_ program exists using [os.path.isfile](https://docs.python.org/3/library/os.path.html#os.path.isfile) to check if a file called _dna.py_ exists:

```
def test_exists() -> None:
    """ Program exists """

    assert os.path.exists(PRG)
```

We can use the Python [assert](https://docs.python.org/3/reference/simple_stmts.html#index-18) statement that will raise an exception (error) when the given expression evaluates to a `False` (ish) value (given that Python has no true Boolean type).
In the Python REPL, the assert with `False` raises an `AssertionError` exception:

```
>>> assert False
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

The statement succeeds with a `True` value (or any non-`False`-ish value):

```
>>> assert True
```

The next test ensures that the program dies when run with zero or two or more command-line arguments. 
Specifically, the program should halt and print a helpful statement on proper _usage_:

```
$ ./dna.py
usage: dna.py DNA

$ ./dna.py ACG GGC
usage: dna.py DNA
```

Additionally, the [POSIX](https://pubs.opengroup.org/onlinepubs/9699919799/) specifies that a program's exit value of zero _conventionally indicates successful termination_.
In `bash` (and `zsh` and most shells), we can inspect the variable `$?` to inspect the exit value of the previous command.
For instance, **`echo Hello`** terminates normally and reports `0`:

```
$ echo Hello
Hello

$ echo $?
0
```

If we run our program with bad inputs, it also reports a nonzero exit value:

```
$ ./dna.py ACG GGC
usage: dna.py DNA

$ echo $?
1
```

The test for this behavior is as follows:

```
def test_usage() -> None:
    """ Prints usage """

    rv, out = getstatusoutput(f'{RUN}')
    assert rv != 0
    assert out.lower().startswith('usage:')
```

The [subprocess.getstatusoutput](https://docs.python.org/3/library/subprocess.html#subprocess.getstatusoutput) function reports the process's return value and `STDOUT`/`STDERR` as a tuple, which I copy into `rv` and `out`, respectively.

* The first assertion verifies that the return value is not zero.
* The second assertion verify that the output begins with the string _usage:_

NOTE: A test may contain as many `assert` statements as you want. When any `assert` fails, the whole test fails.

The next two tests check that the program fails with zero or more than one argument:

```
def test_dies_no_args() -> None:
    """ Dies with no arguments """

    rv, out = getstatusoutput(RUN)
    assert rv != 0
    assert out.lower().startswith('usage:')


def test_dies_too_many_args() -> None:
    """ Dies with too many arguments """

    rv, out = getstatusoutput(f'{RUN} foo bar baz')
    assert rv != 0
    assert out.lower().startswith('usage:')
```

The last test reads DNA strings from the test files and verifies that the program reports the correct output:

```
def test_arg() -> None:
    """ Uses command-line arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        dna = open(file).read()
        rv, out = getstatusoutput(f'{RUN} {dna}')
        assert retval == 0
        assert out == expected
```

As a reminder, the tests are as follows:

```
TEST1 = ('./tests/inputs/input1.txt', '1 2 3 4')
TEST2 = ('./tests/inputs/input2.txt', '20 12 17 21')
TEST3 = ('./tests/inputs/input3.txt', '196 231 237 246')
```

So it's as if we are running:

```
>>> file = './tests/inputs/input1.txt'
>>> expected = '1 2 3 4'
>>> dna = open(file).read()
>>> dna
'ACCGGGTTTT\n'
>>> rv, out = getstatusoutput(f'{RUN} {dna}')
>>> rv
0
>>> out
'1 2 3 4'
>>> assert rv == 0
>>> assert out == expected
```

## Unit Tests

As you get more comfortable with Python, you'll start to write functions to break your code into smaller, more understandable/composable/testable chunks.
The _dna1.py_ is a good starting point for our program.
While it passes the integration tests, it does not contain any functions that require a unit test:

```
#!/usr/bin/env python3
"""
A program to report the frequency of DNA nucleotides
"""

import sys
import os

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
```

To test this program, copy the file to _dna.py_:

```
$ cp dna1.py dna.py
```

Next, run `pytest`, which will recursively search from the current working directory for any files named like "_test.py":

```
$ pytest
================================= test session starts =================================
platform darwin -- Python 3.12.4, pytest-8.3.2, pluggy-1.5.0
rootdir: /Users/kyclark/work/pfb2024/workshops/testing
plugins: flake8-1.2.2, pylint-0.21.0, mypy-0.10.3, anyio-4.4.0
collected 5 items

tests/dna_test.py .....                                                         [100%]

================================== 5 passed in 0.32s ==================================
```

I prefer to run `pytest` with the `-v` (verbose) flag to see more output along with the `-x` flag to halt testing on the first failing test.
You can put the flags in any order, and because they are single-character flags, combine them into `-xv` or `-vx`:

```
$ pytest -vx
================================= test session starts =================================
platform darwin -- Python 3.12.4, pytest-8.3.2, pluggy-1.5.0 -- /Library/Frameworks/Python.framework/Versions/3.12/bin/python3
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/pfb2024/workshops/testing
plugins: flake8-1.2.2, pylint-0.21.0, mypy-0.10.3, anyio-4.4.0
collected 5 items

tests/dna_test.py::test_exists PASSED                                           [ 20%]
tests/dna_test.py::test_usage PASSED                                            [ 40%]
tests/dna_test.py::test_dies_no_args PASSED                                     [ 60%]
tests/dna_test.py::test_dies_too_many_args PASSED                               [ 80%]
tests/dna_test.py::test_arg PASSED                                              [100%]

================================== 5 passed in 0.32s ==================================
```

The following `for` loop is something that could go into a function that we could test:

```
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
```

It will be easier to add a "count" function if we put the other parts of the program into a function.
Many languages like C/C++/Rust will always start in a `main` function, and it's common (but not required) to do this in Python.
The _dna2.py_ shows a typical way to organize a Python executable program to call `main` when the program is executed:

```
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
```

There is no discernible difference in how this program works.
If I **`cp dna2.py dna.py`** and run `pytest`, it passes the integration tests.

Next, look at _dna3.py_ for how I might write a `count` function that takes the `dna` variable as an argument and returns a 4-tuple with the counts for A, C, G, and T:

```
def count(dna):
    """ Count bases in DNA """

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

    return (count_a, count_c, count_g, count_t)
```

Following is a test for this function that will be executed by Pytest because it begins with "test_".
As with the integration tests, I use `assert` statements to verify that the function returns the expected results for various inputs:

```
def test_count():
    """ Test count """

    assert count('') == (0, 0, 0, 0)
    assert count('123XYZ') == (0, 0, 0, 0)
    assert count('A') == (1, 0, 0, 0)
    assert count('C') == (0, 1, 0, 0)
    assert count('G') == (0, 0, 1, 0)
    assert count('T') == (0, 0, 0, 1)
    assert count('ACCGGGTTTT') == (1, 2, 3, 4)
```

I can tell Pytest to execute the test like so:

```
$ pytest -xv dna3.py
================================= test session starts =================================
platform darwin -- Python 3.12.4, pytest-8.3.2, pluggy-1.5.0 -- /Library/Frameworks/Python.framework/Versions/3.12/bin/python3
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/pfb2024/workshops/testing
plugins: flake8-1.2.2, pylint-0.21.0, mypy-0.10.3, anyio-4.4.0
collected 1 item

dna3.py::test_count PASSED                                                      [100%]

================================== 1 passed in 0.00s ==================================
```

The `main` function changes as follows:

```
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        sys.exit("usage: {} DNA".format(os.path.basename(sys.argv[0])))

    count_a, count_c, count_g, count_t = count(args[0])

    print(count_a, count_c, count_g, count_t)
```

Again, I can copy the _dna3.py_ program to _dna.py_ and run `pytest` to verify this progr still passes the integration tests.

Now that I have a `count` function and test, I can _refactor_ this function to improve it (for certain values of _improve_).
For instance, the _dna4.py_ uses `str.count`:

```
def count(dna):
    """ Count bases in DNA """

    return (dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))
```

This is the only difference, which I can verify using the `diff` program:

```
$ diff dna3.py dna4.py
4c4
< This version introduces a count() function and unit test
---
> The count() function in this version uses str.count()
26,35c26
<     count_a, count_c, count_g, count_t = 0, 0, 0, 0
<     for base in dna:
<         if base == 'A':
<             count_a += 1
<         elif base == 'C':
<             count_c += 1
<         elif base == 'G':
<             count_g += 1
<         elif base == 'T':
<             count_t += 1
---
>     return (dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))
37d27
<     return (count_a, count_c, count_g, count_t)
39d28
<
```

I can run **`pytest dna4.py`** to verify my unit test still passes and copy the file to _dna.py_ and run the integration tests.

There are many ways to count values in Python, and _dna5.py_ shows how to use a basic Python dictionary to associate the nucleotides to integer values representing their frequency. 
Again, `pytest dna5.py` verify that the following function passes the same unit tests:

```
def count(dna):
    """ Count bases in DNA """

    counts = {}
    for base in dna:
        if base not in counts:
            counts[base] = 0
        counts[base] += 1

    return (counts.get('A', 0),
            counts.get('C', 0),
            counts.get('G', 0),
            counts.get('T', 0))
```

Finally, I will demonstrate that `collections.Counter` is an external module you can use to count the frequency of objects (producing what is commonly called a _bag_).
The best code is code you don't write, and our unit test verifies that new function passes:

```
def count(dna):
    """ Count bases in DNA """

    counts = Counter(dna)
    return (counts.get('A', 0), counts.get('C', 0), counts.get('G', 0),
          counts.get('T', 0))
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
