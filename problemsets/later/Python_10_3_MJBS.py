#!env/bin/bash python3
import re
import sys
#Problem set 10, number 3
# Modify your function so that it takes two arguments, the DNA string and the max length of each line.

# INPUT:
# dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
# width = 80

dna2 = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'


DNA_string_list = []
final_dna = ''
list_lines = []
def sixty_per_line(DNA_string):
    try:
        global final_dna
        n = 0
        charnum = int(sys.argv[1])
        
        #print(length_DNA)
        if re.findall(r"\s", DNA_string):
            DNA_string_list = DNA_string.rsplit("\n")
            #print(len(DNA_string_list))
            for elem in DNA_string_list:
                final_dna += elem
            #print(final_dna)
            while n < len(final_dna):
                list_lines.append(final_dna[n:n+charnum])
                n = n + charnum
        else:
            length_DNA = len(DNA_string)
            while n < length_DNA:
                list_lines.append(DNA_string[n:n+charnum])
                n = n + charnum
    except IndexError:
        print("please provide a number")
    return list_lines
sixty_per_line(dna2)
for elem in list_lines:
    print(elem)