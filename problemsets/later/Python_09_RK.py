#!/usr/bin/env python3

import sys


#Throw and handle (try/except) the exception

#if no input is provided
#if the file cannot be opened
#if the file does not end in '.fasta' or '.fa' or '.nt'
#if a non ATGCN charcter is found in the sequence

#If raising more than one ValueError, define each as it's own class to handle them
class NotFASTAFile(Exception):
    pass

class NonNTchar(Exception):
    pass

#fasta_file_input='pfb2024/pfb2024/files/Python_06.fasta'
try:
    #did they provide a file? if not, this will raise an IndexError
    fasta_file_input=sys.argv[1]

    #is the file a fasta file? if not, raise the custom NotFASTAFile exception
    if not fasta_file_input.endswith(('.fasta','.fa','.nt')):
       raise NotFASTAFile(f"{fasta_file_input} doesn't look to be a FASTA file")
    
    #is the file openable? if not, raise an IOError (Input/Output)
    #Also, read through file and collect the DNA sequences into temp_nt_holder
    #this holder just gathers all NTs so you can check if they have non-NT characters
    temp_nt_holder=''
    with open(fasta_file_input, 'r') as file:
       for line in file:
            line=line.rstrip()
            if line.startswith('>'):
                next
            else:
                temp_nt_holder+=line
    
    #this pulls out the specified nt's and if there's anything else, raises an error
    if temp_nt_holder.strip('ATGCN'):
        raise NonNTchar
    else:
        next

    #If everything passes, let them know that the parser is good to go
    print(f"Parsing {fasta_file_input}")

# They forgot to put a file argument
except IndexError:
   print('Please provide a file name')

# The file can't be found or opened
except IOError:
   print(f'Cannot find {fasta_file_input}, please check file path')

# The file doesn't have the right file extension
except NotFASTAFile:
  print(f"{fasta_file_input} doesn't look to be a FASTA file, FASTA files end with '.fasta', '.fa', or '.nt'")

# Might not be a DNA sequence, or is messed up
except NonNTchar:
    print(f'{fasta_file_input} has non-nucleotide characters, double check your file.')

#If no exceptions are raised, continue with your fasta parser
else:
    fasta_dict={}
    with open(fasta_file_input, 'r') as file:
        for line in file:
            line=line.rstrip()
            if line.startswith('>'):
                key=line.strip('>')
                fasta_dict[key]=''
            else:
                fasta_dict[key]+=line
    print(fasta_dict)
