#!env/bin/bash python3
import sys
import re

#python Problem set 9 
#raising exceptions and testing for errors

# Add in exception handling to a script from Problem Set 8 or any script you have written that uses I/O to open and read a FASTA file
# Hnadle:
#if no input is provided
# if the file cannot be opened
# if the file does not end in '.fasta' or '.fa' or '.nt'
# if a non ATGCN charcter is found in the sequence

#defining the variable to store the filename that the user inputs
file = ''
c = 0
#defining the NotFastaError as an exception to raise later
class NotFastaError(Exception):
    pass
#defining the NotASequenceFileError as an exception to raise later
class NotASequenceFileError(Exception):
    pass
try:
    file = sys.argv[1]
    print("User provided file name:", file)
    if not file.endswith((".fasta", ".fa", ".nt")): 
        raise NotFastaError("Not a fasta file")
    else:    
        with open(file, "r") as fasta:
            for line in fasta:
                line = line.rstrip()
                line = line.upper()
                if re.findall(r"^>", line):
                    #print(re.findall(r"^>", line)) #^>\w+.*
                    continue
                elif re.findall(r"(^[ATGCN])\S\D[ATGCN]+",line):
                    if re.findall(r"(^[ATGCN])\S\D[ATGCN]+",line):
                        print(line)
                    else:
                        raise NotASequenceFileError("A non ATGCN charcter is found in the sequence")
except IndexError:
    print("Please provide a file name")
except NotFastaError:
    print("Please provide a file that ends with .fasta, .fa or .nt")
except NotASequenceFileError:
    print("Please provide a DNA sesquence .fasta file")
except IOError as ex:
    print(f"Can't find file: {file}, {ex}")