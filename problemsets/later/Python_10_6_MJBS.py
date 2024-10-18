#!env/bin/bash python3
import re
import sys
#Problem set 10, number 6

# Create a new function that computes and returns the reverse complement of a sequence
# it will take a DNA sequence without spaces and no header as an argument and return the reverse complement, with no spaces and no header.
# example revComp_sequence = get_reverse_complement(dna)


def reverseComplement(DNA_string):
        complement_seq = ''
        count = 0 
        for count in range(0, len(DNA_string)):
            if DNA_string[count] == 'A':
                complement_seq = complement_seq + 'T'
            elif DNA_string[count] == 'T':
                complement_seq = complement_seq + 'A'
            elif DNA_string[count] == 'C':
                complement_seq = complement_seq + 'G'
            else:
                complement_seq = complement_seq + 'C'
            count = count + 1
        reverse_complement = complement_seq[::-1]
        return reverse_complement


#defining the variable to store the filename that the user inputs
file = ''
DNA_string_list = []
final_dna = ''
saving_fasta_in_dir = {}
#defining the NotFastaError as an exception to raise later
class NotFastaError(Exception):
    pass
#defining the NotASequenceFileError as an exception to raise later
class NotASequenceFileError(Exception):
    pass

#making sure a fasta format is provided
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
                    #save the header into the dictionary
                    header = line
                    saving_fasta_in_dir[header] = ''
                elif re.findall(r"(^[ATGCN])\S\D[ATGCN]+",line):
                    saving_fasta_in_dir[header] = line
                else:
                    raise NotASequenceFileError("A non ATGCN charcter is found in the sequence")
            #print(saving_fasta_in_dir)
            for key in saving_fasta_in_dir:
                print(f" The reverse complement of {saving_fasta_in_dir[key]} is : {reverseComplement(saving_fasta_in_dir[key])}")
except IndexError:
    print("Please provide a file name")
except NotFastaError:
    print("Please provide a file that ends with .fasta, .fa or .nt")
except NotASequenceFileError:
    print("A non ATGCN charcter is found in the sequence. Please provide a DNA sesquence .fasta file")
except IOError as ex:
    print(f"Can't find file: {file}, {ex}")

