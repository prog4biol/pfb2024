#!/usr/bin/env python3

import subprocess

######
#INPUT: a string of DNA without newlines
#OUTPUT: a string of DNA with lines no more than 60 nucleoties long

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTGCTCAAGAC\nTGGCGCTAAAAGTTTTGAGCTTCTGCAAGACTGGCGCTAAAAGTTTTGAGCTTCTGAGCTTCTGAGCTTCCTGGCGCTAAAAGTTTTGAGCTTCT'

def nt_60_dna(input):
    #remove any \n
    input=input.replace('\n','')
    dna_60_nt_out = ''
    x=0
    
    #call x as range from 0 to length of the string
    #every time the loop runs, add 60 to x
    for x in range(0,len(input), 60):

       #print(f'{input[x:x+60]}\n')
        
        #pull out x - x+60 from the string
        #also print the x count/nt position
        dna_60_nt_out+=f'{input[x:x+60]}\t{x}\t{x+59}\t{len(input[x:x+60])}\n'
        print(x)
        
    print(dna_60_nt_out)

nt_60_dna(dna)



######
#Modify your function so that it takes two arguments, the DNA string and the max length of each line.
def any_nt_func(seq_input, maxlen):
    #remove any \n
    seq_input=seq_input.replace('\n','')
    dna_any_nt_out = ''
    x=0
    
    #call x as range from 0 to length of the string
    #every time the loop runs, add maxlen to x
    for x in range(0,len(seq_input), maxlen):

       #print(f'{seq_input[x:x+maxlen]}\n')
        
        #pull out x - x+maxlen from the string
        #also print the nt position and line lengths
        dna_any_nt_out+=f'{seq_input[x:x+maxlen]}\t{x}\t{x+(maxlen-1)}\t{len(seq_input[x:x+maxlen])}\n'
        print(x)
        
    print(dna_any_nt_out)
#any_nt_func(dna,32)


#####
#Modify your script so that it can take two command line arguments: FASTA file name, Max length of each line
def any_nt_func(fasta_input_file, maxlen):

    fasta_dict={}
    with open(fasta_input_file, 'r') as fasta_input:
        for line in fasta_input:
            line=line.rstrip()

            #assign sequence keys 
            if line.startswith('>'):
                seq_key=line
                fasta_dict[seq_key]=''
            
            #for dna lines
            else:

                #define range of indices
                #this for loop runs for the entire line until it hits the top of the range len(line)
                #then moves to the next line
                for i in range(0,len(line),maxlen):

                    #print(i, len(line))
                    
                    #subset lines to index lengths
                    dna_output=f'{line[i:i+maxlen]}\n'

                    #add each into the dictionary value
                    fasta_dict[seq_key]+=dna_output
    #print(fasta_dict)
    
    #Use a list comprehension to format >key \n value for each sequence entry
    func_output=[f'{seq_key}\n{dna_output}' for seq_key, dna_output in fasta_dict.items()]

    #print the list as a string with new lines
    print('\n'.join(func_output))

any_nt_func('tester_fasta.fa',22)


######
#Create a new function that calculates the GC content of a DNA sequence.
#it will take a DNA sequence without spaces and no header as an argument 
# and return the percentage of nucleotides that are a G or C

gc_input_seq='TGGGATTGGGGTTTTCCCCTCCCATGTGCTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTGCAAGACTGGCGCTAAAAGTTTTGAGCTTCTGAGCTTCTGAGCTTCCTGGCGC'
gc_small_test_6G5C='TATACGGATCGGTTCTGGCC'
def calc_GC_content(seq_input):

    gc_count=seq_input.count('G')+seq_input.count('C')
    print(gc_count)
    
    total_len=len(seq_input)
    print(total_len)

    print(f'GC content is: {gc_count/total_len}')

calc_GC_content(gc_input_seq)

#####
#Create a new function that computes and returns the reverse complement of a sequence

def rev_comp(seq):
    # Reverse Complement of 'seq'
    reverse_seq = seq[::-1]
    #print(seq[0:5],reverse_seq[-5:])

    #define complement
    complement_key={'A':'T','T':'A','C':'G', 'G':'C'}

    reverse_complement=''
    for nt in reverse_seq:
        new_nt=complement_key[nt][0]
        reverse_complement+=new_nt
    
    print(seq)
    print(reverse_complement)

rev_comp(gc_small_test_6G5C)


