#!env/bin/bash python3
import re
import sys
#Problem set 10, number 4

# Modify your script so that it can take two command line arguments:

# FASTA file name
# Max length of each line
# The script should reformat every sequence in the file to the specified max line length. Make sure your output is in proper FASTA format.
#dna2 = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

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


def sixty_per_line(DNA_dictinoray):
    try:
        global final_dna
        charnum = int(sys.argv[2])
        
        #print(length_DNA)
        for key in DNA_dictinoray:
            #print(key)
            DNA_string = DNA_dictinoray[key]
            #print(DNA_string)
            list_lines = []
            n = 0
            if re.findall(r"\s", DNA_string):
                DNA_string_list = DNA_string.rsplit("\n")
                print("found new line in sequence",len(DNA_string_list))
                for elem in DNA_string_list:
                    final_dna += elem
                #print(final_dna)
                while n < len(final_dna):
                    list_lines.append(final_dna[n:n+charnum])
                    n = n + charnum
                DNA_dictinoray[key] = list_lines
                #print(DNA_dictinoray)
            else:
                length_DNA = len(DNA_string)
                #print(length_DNA)
                while n < length_DNA:
                    list_lines.append(DNA_string[n:n+charnum])
                    n = n + charnum
                DNA_dictinoray[key] = list_lines
                #print(DNA_dictinoray)
    except IndexError:
        print("please provide a number aside of the file")
    return DNA_dictinoray

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
            saving_fasta_in_dir = sixty_per_line(saving_fasta_in_dir)
            for key in saving_fasta_in_dir:
                print(key)
                for elem in saving_fasta_in_dir[key]:
                    print(elem)
except IndexError:
    print("Please provide a file name")
except NotFastaError:
    print("Please provide a file that ends with .fasta, .fa or .nt")
except NotASequenceFileError:
    print("A non ATGCN charcter is found in the sequence. Please provide a DNA sesquence .fasta file")
except IOError as ex:
    print(f"Can't find file: {file}, {ex}")
