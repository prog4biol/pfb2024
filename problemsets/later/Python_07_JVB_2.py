#!/usr/bin/env python3

import re
import sys

input_filename = sys.argv[1]
replacement_string = sys.argv[2]

input_file = open(input_filename, 'r')

# since our pattern never changes, compile it for use up-front:
pattern = re.compile(r'Nobody', flags=re.IGNORECASE)

# BONUS: To tell the user which line we are on, we need to
# initialize a variable *above* the loop so that we can
# increment it each iteration:
line_number = 0
for line in input_file:
    line = line.rstrip()

    line = pattern.sub(replacement_string, line)

    print(line)

# nice and tidy:
input_file.close()
