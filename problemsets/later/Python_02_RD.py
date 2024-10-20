#!/usr/bin/env python3


# A. Use the Interactive Interpretor to test to see if you can find an 'ATG' in the following DNA string:

# >>> 'ATG' in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'


# B. How about 'TTT'?

# >>> 'TTT' in 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'


# C. If you didn't already save the DNA string to a variable, do that now and redo part A and B.


# >>> dna_string = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'

# >>> 'ATG' in dna_string
# >>> 'TTT' in dna_string

#################################################################################################3

# 1. Write a script that

#       Assigns a value to a variable
#       Has a if/else statment in which:
#       It prints out a confirmation of truth if the value is true, like "Aye Captain" or something less sea worthy
#       It prints out "Not True" if the value is not true. (so boring)


sea_worthy_statement = 'Arrrgh! I need mi peg leg'

if sea_worthy_statement != 'Arrrgh! I need mi peg leg':
    print('Yer a true Captain')
else:
    print('Boring...')

# 2. Make sure to commit your changes along the way. You can wait until the end to push them to your remote repo, if you like, or you can do it now.


## git add Python
## git commit -m 'updates'
## git push

# 3. Create a script that has an if/else statement with the following conditions (remember to write a little bit at a time and test it

test_number = 5

if test_number >= 0:
    print('positive')
else:
    print('negative')

# 4. Add an elif to test if the number is equal to 0. Save it and run it.

test_number = 5

if test_number > 0:
    print('positive')
elif test_number == 0:
    print('number is 0')
else:
    print('negative')

# 5. Add nested tests to your last script

#   if it is positive, in addition to printing "positive"
#   test if it is smaller than 50
#   save it and run it

if test_number > 0:
    print('positive')

elif test_number < 50:
    print('number is smaller than 50')

elif test_number == 0:
    print('number is 0')

else:
    print('negative')

# 6. Add more nested tests to your script.

#   if it is smaller than 50
#   test if the number is even
#   if it is smaller than 50 and even, print "it is an even number that is smaller than 50"
#   save it and run it

if test_number > 0:
    print('positive')

elif test_number < 50:
    print('number is smaller than 50')

elif (test_number % 2) == 0:
    print('number is even')

elif (test_number % 2) == 0 and test_number > 50:
    print('number is even and smaller than 50')

elif test_number == 0:
    print('number = 0')

else:
    print('negative')

# 7. Add more nested tests.

#   if it is larger than 50,
#   test if the number is divisible by 3
#   if the number is larger than 50 and divisible by 3, print "it is larger than 50 and divisible by 3"
#   save it and run it

if test_number > 0:
    print('positive')

elif test_number < 50:
    print('number is smaller than 50')

elif (test_number % 2) == 0:
    print('number is even')

elif test_number % 2 and test_number > 50:
    print('number is even and smaller than 50')

elif test_number % 3 and test_number < 50:
    print('number is divisible by 3 and larger than 50')

elif test_number == 0:
    print('number = 0')

else:
    print('negative')


# 9. Write a new script that does all the testing in 3-8, but gets the value being tested from the command line (use sys.argv) and stores it in a variable. Add in a print statement that reminds the user what number is being tested.
import sys

test_number = int(sys.argv[1])

print(f'Number being tested is: {test_number}')


if test_number > 0:
    print('number is positive')

elif test_number < 50:
    print('number is smaller than 50')

elif (test_number % 2) == 0:
    print('number is even')

elif (test_number % 2) == 0 and test_number > 50:
    print('number is even and smaller than 50')

elif (test_number % 3) == 0 and test_number < 50:
    print('number is divisible by 3 and larger than 50')

elif test_number == 0:
    print('number = 0')

else:
    print('number is negative')
