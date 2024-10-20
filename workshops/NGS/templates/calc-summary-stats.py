#!/usr/bin/env python3

# import the os module to trim off the file path off the of
# the script name (to get the path "basename").
import os

# import sys to take positional arguments from the command
# line
import sys

# I like to build these usage functions that allow me to print
# the same command line usage synopsys under different input
# conditions:
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
    # "infile.depth", not "<infile.depth>"
    stream.write(f"""
Usage: {program} <input.tsv>

{message}""")

    # Return an exit status reflective of whether the code 
    # execution resulted in an error (> 0) or not (= 0):
    sys.exit(status)


    
def calc_mean(frequency):
    # Using weighted mean formula:
    #   mean_w = sum {weight[j] * x[j]} / n, for i in 0 -> n
    #       where weight[j] is the frequency of the x[j]-th depth value:
    #
    #  See: https://en.wikipedia.org/wiki/Weighted_arithmetic_mean

    # ***********************************************
    # ** WRITE CODE TO CALCULATE THE WEIGHTED MEAN **
    # ***********************************************
    
    return mean



def calc_sd(frequency, mean):
    # Using weighted mean, calculate stddev with formula:
    #   stddev_w = sqrt [ sum {weight[x[i]] * (x[i] - u)^2} / n ], for i in 0 -> n
    #       where weight[j] is the frequency of the x[j]-th depth value:
    #
    #  See: https://en.wikipedia.org/wiki/Weighted_arithmetic_mean

    # ****************************************
    # ** WRITE CODE TO CALCULATE THE STDDEV **
    # ****************************************
    
    return sd



def calc_stats_from_fileobj(infile):
    # Our input file has three columns, which contain the chromosome name,
    # 1-based chromosome position, and read depth (respectively). Parse
    # to obtain the third column and calculate mean and stddev.
    # chrI	1	15
    # chrI	2	15
    # chrI	3	14
    # chrI	4	16
    # chrI	5	16

    # The mean can be calculated as:
    #   u = sum {x[i]} / n, over i = 0 -> n
    # or, using weighted mean formula:
    #   u_w = sum {weight[j] * x[j]} / n, over j = 0 -> n
    #       where weight[j] is the frequency of the x[j]-th depth value:

    # The stddev can be calculated as:
    #   s = sqrt [ sum {(x[i] - u)^2} / n ], over i = 0 -> n
    # or, using weighted stddev formula:
    #   s_w = sqrt [ sum {weight[j] * (x[i] - u)^2} / n ], over j = 0 -> max(x)
    #       where weight[j] is the frequency of the x[j]-th depth value:

    counts = {}
    for line in infile:
        # each line is a string, ex: "chr\t12345\t15\n"

        # ****************************************************************
        # ** WRITE CODE TO PARSE THE INFORMATION WE NEED FROM EACH LINE **
        # ****************************************************************
        
    mean = calc_mean(counts)
    sd = calc_sd(counts, mean)
        
    # return both mean and sd by wrapping them in a tuple!
    return (mean, sd)



def main(arguments):
    # In programming convention, the main() function is where command-line
    # inputs are handled and the usage message is emitted when the user gives
    # bad input arguments. Once our script validates it is happy with its
    # inputs, proceed to call the core script function:
    # calc_stats_from_fileobj()
    if len(arguments) == 0:
        # If the user gives no arguments, print the usage synopsis nicely:
        usage(status=0)
        
    elif len(arguments) != 1:
        # If the user gives too few or too many arguments, complain loudly:
        usage(
            message="Unexpected number of arguments",
            status=1
        )

    filename = arguments[0]
    # Attempt to open a fastq file for reading:
    idepth = open(filename, 'r')

    # We want to print to the screen (which python does by default), but
    # we can build in some flexibility by coding in handling an output
    # file variable explicitly:
    ostats = sys.stdout

    mean, sd = calc_stats_from_fileobj(idepth)

    # Write out the filename with mean and sd, rounded to the hundredths
    # place (2 significant figures after the decimal):
    print(f"filename\tmean\tsd", file=ostats)
    print(f"{filename}\t{mean:.2f}\t{sd:.2f}", file=ostats)
    
    # finally, when working with files, close your files explicitly:
    idepth.close()
    ostats.close()


if __name__ == '__main__':
    main(sys.argv[1:])
