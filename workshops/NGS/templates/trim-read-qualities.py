#!/usr/bin/env python3

# import the os module to trim off the file path off the of
# the script name (to get the path "basename").
import os

# import sys to take positional arguments from the command
# line
import sys


def usage(message=None, status=1, stream=sys.stderr):
    # another way to get the program name:
    program = os.path.basename(__file__)

    # format a pretty usage message to help the user learn
    # how to run your code. The more user-friendly your code
    # is, the more likely others are to use it
    message = '' if message is None else f'ERROR: {message}\n\n'

    # In programming convention arguments with <> around them
    # denote *required* arguments, while [] denote *optional*
    # arguments, and does not mean those characters need to be
    # included in the file name: i.e., the user should input
    # "infile.fastq", not "<infile.fastq>"
    stream.write(f"""
Usage: {program} <input.fastq> <min-qual>

{message}""")

    # Return an exit status reflective of whether the code 
    # execution resulted in an error (> 0) or not (= 0):
    sys.exit(status)



def trim_reads_from_fileobj(min_quality_threshold=-1, infile=sys.stdin, outfile=sys.stdout):
    for line in infile: 

        # *********************************************************
        # ** WRITE CODE TO PARSE A FASTQ FILE AND TRIM THE READS **
        # *********************************************************

        print(header, file=outfile)
        print(trimmed_seq, file=outfile)
        print(plus_sign, file=outfile)
        print(trimmed_qual, file=outfile)

        

def main(arguments):
    # In programming style, the main() function is where command-line inputs
    # are handled and the usage message is emitted when the user gives bad
    # input arguments. Once our script validates it is happy with its inputs,
    # proceed to call the core script function: trim_reads_from_file()

    
    if len(arguments) == 0:
        # If the user gives no arguments, print the usage synopsis nicely:
        usage(status=0)
        
    elif len(arguments) != 2:
        # If the user gives too few or too many arguments, complain loudly:
        usage(
            message="Unexpected number of arguments",
            status=1
        )

    # Attempt to open a fastq file for reading:
    ifastq = open(arguments[0], 'r')

    # We want to print to the screen (which python does by default), but
    # we can build in some flexibility by coding in handling an output
    # file variable explicitly:
    ofastq = sys.stdout

    # The second argument to our script *should* be an integer, but if the
    # user provides, say, a string, then we should catch the error gracefully
    # and tell the user nicely that we expect an integer instead:
    try:
        # Calling int() raises a ValueError if it cannot convert our
        # input arguments[1] (which is a string from sys.argv) into
        # an integer:
        min_quality_threshold = int(arguments[1])
    except ValueError:
        usage(
            message="<min-qual> argument must be an integer",
            status=1
        )

    trim_reads_from_fileobj(min_quality_threshold, ifastq, ofastq)

    # finally, when working with files, close your files explicitly:
    ifastq.close()
    ofastq.close()


if __name__ == '__main__':
    main(sys.argv[1:])
