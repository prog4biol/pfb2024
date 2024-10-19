#!env/bin/bash python3
import re
import sys
#Problem set 10, number 5

# Create a new function that calculates the GC content of a DNA sequence.
# it will take a DNA sequence without spaces and no header as an argument and return the percentage of nucleotides that are a G or C.
# example percentGC = gc_conent('CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA') or percentGC = gc_content(dna)
DNA_seq = ""

def GC_content(DNA_string):
        DNA_string_numC = DNA_string.count("C")
        DNA_string_numG = DNA_string.count("G")
        DNA_string_GC_content = DNA_string_numC + DNA_string_numG / len(DNA_string)
        return DNA_string_GC_content

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
                print(f" GC content of {saving_fasta_in_dir[key]} is : {GC_content(saving_fasta_in_dir[key])}")
except IndexError:
    print("Please provide a file name")
except NotFastaError:
    print("Please provide a file that ends with .fasta, .fa or .nt")
except NotASequenceFileError:
    print("A non ATGCN charcter is found in the sequence. Please provide a DNA sesquence .fasta file")
except IOError as ex:
    print(f"Can't find file: {file}, {ex}")

