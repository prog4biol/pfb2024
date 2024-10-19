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
$ ./dna1.py
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

import os                              # 1
import platform                        # 2
from subprocess import getstatusoutput # 3
```

1. The `os` module is for interacting with the operating system.
2. The `platform` module will tell me if the tests are running on Windows
3. The `subprocess` module provides the `getstatusoutput` function for running an external process

Next are some "constant" definitions: 

```
PRG = './dna.py'                                                 # 1
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG # 2
TEST1 = ('./tests/inputs/input1.txt', '1 2 3 4')                 # 3
TEST2 = ('./tests/inputs/input2.txt', '20 12 17 21')
TEST3 = ('./tests/inputs/input3.txt', '196 231 237 246')
```
1. The name of the program I'm testing.
2. How I need to execute the program depending on the OS.
3. Test input files along with the expected results.

Pytest will execute any function with a name that starts with "test_" as a test, and tests in the order they are defined in the file.
The first test checks if the _dna.py_ program exists:

```
def test_exists():
    """ Program exists """

    assert os.path.exists(PRG) # 1
```

1. Use [os.path.isfile](https://docs.python.org/3/library/os.path.html#os.path.isfile) to check if a file called _dna.py_ exists.

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
usage: dna.py [-h] dna
dna.py: error: the following arguments are required: dna

$ ./dna.py ACG GGC
usage: dna.py [-h] dna
dna.py: error: unrecognized arguments: GGC
```

Additionally, the [POSIX](https://pubs.opengroup.org/onlinepubs/9699919799/) specifies that a program's exit value of zero _conventionally indicates successful termination_.
In `bash` (and `zsh` and most shells), we can inspect the variable `$?` for the exit value of the previous command.
For instance, **`echo Hello`** terminates normally and reports `0`:

```
$ echo Hello
Hello

$ echo $?
0
```

If we run our program with bad inputs, it prints usage _and_ reports a nonzero exit value:

```
$ ./dna.py ACG GGC
usage: dna.py DNA

$ echo $?
2
```

The test for this behavior is as follows:

```
def test_usage():
    """ Prints usage """

    rv, out = getstatusoutput(f'{RUN}')     # 1
    assert rv != 0                          # 2
    assert out.lower().startswith('usage:') # 3
```

1. The [subprocess.getstatusoutput](https://docs.python.org/3/library/subprocess.html#subprocess.getstatusoutput) function reports the process's return value and `STDOUT`/`STDERR` as a tuple, which I copy into `rv` and `out`, respectively.
2. The first assertion verifies that the return value is not zero.
3. The second assertion verify that the output begins with the string _usage:_

NOTE: A test may contain as many `assert` statements as you want. When any `assert` fails, the whole test fails.

The next two tests check that the program fails with zero or more than one argument:

```
def test_dies_no_args():
    """ Dies with no arguments """

    rv, out = getstatusoutput(RUN) # 1
    assert rv != 0
    assert out.lower().startswith('usage:')


def test_dies_too_many_args():
    """ Dies with too many arguments """

    rv, out = getstatusoutput(f'{RUN} foo bar baz') # 2
    assert rv != 0
    assert out.lower().startswith('usage:')
```

1. Run the program with no arguments.
2. Run the program with too many arguments.

The last test reads DNA strings from the test files and verifies that the program reports the correct output:

```
def test_arg():
    """ Uses command-line arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        dna = open(file).read()                   # 1
        rv, out = getstatusoutput(f'{RUN} {dna}') # 2
        assert rv == 0                            # 3
        assert out == expected                    # 4
```

1. Open the file and read the input into the `dna` variable.
2. Run the program with the given input.
3. Ensure the return value is 0.
4. Ensure the program's output is the expected value.

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
>>> rv, out = getstatusoutput(f'./dna.py ACCGGGTTTT')
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
#!/usr/bin/env python3 # 1
"""
A program to report the frequency of DNA nucleotides # 2
"""

import argparse # 3

parser = argparse.ArgumentParser(description='Count DNA bases') # 4
parser.add_argument('dna')                                      # 5
args = parser.parse_args()                                      # 6
count_a, count_c, count_g, count_t = 0, 0, 0, 0                 # 7

for base in args.dna: # 8
    if base == 'A':
        count_a += 1
    elif base == 'C':
        count_c += 1
    elif base == 'G':
        count_g += 1
    elif base == 'T':
        count_t += 1

print(count_a, count_c, count_g, count_t) # 9
```

1. The _shebang_ line tells the shell to execute Python.
2. A _docstring_ to explain what the code does.
3. Import the [argparse](https://docs.python.org/3/library/argparse.html) module to validate and parse the command-line arguments.
4. Create an [ArgumentParser](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) object that will handle the arguments.
5. Tell the parser to add a _positional_ argument for the DNA argument.
6. Tell the parser to parse the arguments. The program will fail here and print error messages if the arguments are invalid.
7. Initialize counters for the number of As, Cs, Gs, and Ts.
8. Iterate through each base in the input `args.dna` and increment the correct counter.
9. Print the results, separated by spaces.

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

import argparse

# --------------------------------------------------
def main(): # 1
    parser = argparse.ArgumentParser(description='Count DNA bases')
    parser.add_argument('dna')
    args = parser.parse_args()
    count_a, count_c, count_g, count_t = 0, 0, 0, 0

    for base in args.dna:
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
if __name__ == '__main__': # 2
    main()
```

1. All the code now lives in a `main` function.
2. If the code is being executed as a script, call the `main` function.

****
There's not much difference in the structure of a Python _program_ that you execute and a Python _module_ that can be imported by other Python code. 
Open the REPL and execute the following:

```
>>> import dna1
usage: [-h] dna
: error: the following arguments are required: dna
```

Why did it print the usage?
Because Python executed all the code from top to bottom, saw there were insufficient arguments, and printed the _usage_ statement.
Now run **`import dna2`** and notice there is no execution of the code unless we specifically call the `main` function:

```
>>> import dna2
>>> dna2.main()
usage: [-h] dna
: error: the following arguments are required: dna
```

When you _import_ a module, the _namespace_ (which is stored in the "__name__" variable) is that module's name, e.g., "dna1" or "dna2."
When you _execute_ a program, the namespace is [__main__](https://docs.python.org/3/library/__main__.html), hence this bit of sorcery:

```
if __name__ == '__main__':
    main()
```

Python other such _dunder_ (double-underscore) variables like "__file__".
****

There is no discernible difference in how the _dna2.py_ and _dna1.py_ programs work.
If I **`cp dna2.py dna.py`** and run `pytest`, it passes the integration tests.

Next, look at _dna3.py_ for how I might write a `count` function:

```
def count(dna):                # 1
    """ Count bases in DNA """ # 2

    count_a, count_c, count_g, count_t = 0, 0, 0, 0 # 3
    for base in dna:
        if base == 'A':
            count_a += 1
        elif base == 'C':
            count_c += 1
        elif base == 'G':
            count_g += 1
        elif base == 'T':
            count_t += 1

    return (count_a, count_c, count_g, count_t) # 4
```

1. The function is named `count` and its argument, `dna` is enclosed in the parentheses.
2. This is a docstring for the function.
3. This is the same code as before.
4. The function uses `return` to produce a 4-tuple with the counts for A, C, G, and T.

Following is a test for this function 
I usually place unit tests right below the functions they test.
As with the integration tests, I use `assert` statements to verify that the function returns the expected results for various inputs:

```
def test_count():      # 1
    """ Test count """ # 2

    assert count('') == (0, 0, 0, 0)           # 3
    assert count('123XYZ') == (0, 0, 0, 0)     # 4
    assert count('A') == (1, 0, 0, 0)          # 5
    assert count('C') == (0, 1, 0, 0)          # 6
    assert count('G') == (0, 0, 1, 0)          # 7
    assert count('T') == (0, 0, 0, 1)          # 8
    assert count('ACCGGGTTTT') == (1, 2, 3, 4) # 9
```

1. The prefix "test_" tells Pytest that this is a test.
2. This is the docstring for the function.
3. Check that the functions does not fail on the empty string.
4. Ensure that it returns all zeros when given no nucleotides.
5. Ensure it counts As and returns them in the first position.
6. Ensure it counts Cs and returns them in the second position.
7. Ensure it counts Gs and returns them in the third position.
8. Ensure it counts Ts and returns them in the fourth position.
9. Ensure it counts all the bases and returns them in the correct positions.

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
    parser = argparse.ArgumentParser(description='Count DNA bases')
    parser.add_argument('dna')
    args = parser.parse_args()
    count_a, count_c, count_g, count_t = count(args.dna) # 1

    print(count_a, count_c, count_g, count_t)
```

1. Call the `count` function with the `dna` argument.

Again, I can copy the _dna3.py_ program to _dna.py_ and run `pytest` to verify this progr still passes the integration tests.

Now that I have a `count` function and test, I can _refactor_ this function to improve it (for certain values of _improve_).
For instance, the _dna4.py_ uses `str.count`:

```
def count(dna):
    """ Count bases in DNA """

    return (dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))
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

NOTE: This function currently counts only DNA nucleotides, but I could return a dictionary showing the frequency of _every_ character in an input. This would make the program able to handle any input alphabet including RNA, amino acids, or English text.

Finally, I will demonstrate that `collections.Counter` is an external module you can use to count the frequency of objects (producing what is commonly called a _bag_).
The best code is code you don't write, and our unit test verifies that new function passes:

```
def count(dna):
    """ Count bases in DNA """

    counts = Counter(dna)
    return (counts.get('A', 0), counts.get('C', 0), counts.get('G', 0),
          counts.get('T', 0))
```

## See Also

See the [GitHub repo for Mastering Python for Bioinformatics])https://github.com/kyclark/biofx_python/tree/main/01_dna) for more complete solutions that use `argparse`](https://docs.python.org/3/library/argparse.html) to validate command-line arguments.

## Author

Ken Youens-Clark <kyclark@gmail.com>
