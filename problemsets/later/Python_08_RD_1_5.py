#!/usr/bin/env python3

import sys

### 1.  Take a multi-FASTA Python_08.fasta file from user input and calculate the nucleotide composition for each sequence. Use a datastructure to keep count. Print out each sequence name and its compostion in this format seqName\tA_count\tT_count\tG_count\C_count

fasta_file = sys.argv[1]


seqs = {}

with open(fasta_file, 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            gene_name = line.split(' ')[0][1:]
            seqs[gene_name] = {'A':0,'T':0,'G':0,'C':0}
        else:
            for nt in line:
                seqs[gene_name][nt] += 1
"""                
for gene_name in seqs:
    print(f"Gene Name: {gene_name}",
    f"A count: {seqs[gene_name]['A']}",
    f"T count: {seqs[gene_name]['T']}",
    f"G count: {seqs[gene_name]['G']}",
    f"C count: {seqs[gene_name]['C']}", sep = "\t")
"""

### 2. Write a script that takes a multi-FASTA file Python_08.fasta from user input and breaks each sequence into codons (every three nucleotides is a codon) in just the first reading frame. Your output should look like this
"""
 seq1-frame-1-codons
 CAT GCT TGA GTC
"""

seqs = {}

with open(fasta_file, 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            sequence = ""
            gene_name = line.split(' ')[0][1:]
            seqs[gene_name] = sequence
        else:
            sequence += line
            
        seqs[gene_name] = sequence


### Write the output to a file called 'Python_08.codons-frame-1.nt'.

with open('Python_08.codons-frame-1.nt', 'w') as reading_frame1:
    for gene in seqs:
        codons = []
        for i in range(0,len(seqs[gene]),3):

            codons.append(seqs[gene][i:i+3])
            
        print(gene+'-'+'frame-1-codons\n',*codons, sep = ' ', file = reading_frame1)



### 3. Now produce codons in the first three reading frames for each sequence and print out ids and sequence records for each frame and print to a file called 'Python_08.codons-3frames.nt


seqs = {}

with open(fasta_file, 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            sequence = ""
            gene_name = line.split(' ')[0][1:]
            seqs[gene_name] = sequence
        else:
            sequence += line

        seqs[gene_name] = sequence



with open('Python_08.codons-3frames.nt', 'w') as reading_frames:
    for gene in seqs:    
        for frame in range(3):
            codons = []
            for i in range(frame,len(seqs[gene]),3):

                codons.append(seqs[gene][i:i+3])

            print(gene+'-'+f'frame-{frame+1}-codons\n',*codons, sep = ' ', file = reading_frames)


### 4. Now reverse complement each sequence and print out all six reading frames to a file called 'Python_08.codons-6frames.nt'

seqs = {}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

with open(fasta_file, 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            sequence = ""
            gene_name = line.split(' ')[0][1:]
            seqs[gene_name] = sequence
        else:
            sequence += line.upper()
            

        seqs[gene_name] = sequence

with open('Python_08.codons-6frames.nt', 'w') as reading_frames:
    for gene in seqs:
        for frame in range(3):
            codons = []
            rev_codons = []
            for i in range(frame,len(seqs[gene]),3):
                codon = seqs[gene][i:i+3]
                rev_codon = seqs[gene][::-1][i:i+3]

                codons.append(codon)
                rev_codon = "".join(complement.get(base,base) for base in rev_codon)
                rev_codons.append(rev_codon)

                if len(codons[-1]) < 3:
                    codons.pop()
                if len(rev_codons[-1]) < 3:
                    rev_codons.pop()

            print(gene+'-'+f'frame-{frame+1}-codons\n',*codons, '\n'+gene+'-'+f'reverseframe-{frame+1}-codons\n',*rev_codons, sep = ' ', file = reading_frames)

### 5. Translate each of the six reading frames into amino acids. Create one file for which you print the six reading frames (Python_08.codons-6frames.nt) and one file for which you print the translation of the six reading frames (Python_08.translated.aa). Use the following translation table:

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}
seqs = {}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

nt_file=open('Python_08.codons-6frames.nt', 'w') 
tr_file=open('Python_08.translated.aa', 'w')

with open(fasta_file, 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            sequence = ""
            gene_name = line.split(' ')[0][1:]
            seqs[gene_name] = sequence
        else:
            sequence += line.upper()


        seqs[gene_name] = sequence


with open('Python_08.codons-6frames.nt', 'w') as nt_file, open('Python_08.translated.aa', 'w') as tr_file:
    for gene in seqs:
        for frame in range(3):
            codons = []
            rev_codons = []
            translated_codons = []
            translated_rev_codons = []
            for i in range(frame,len(seqs[gene]),3):
                codon = seqs[gene][i:i+3]
                rev_codon = seqs[gene][::-1][i:i+3] # Reverse the sequence 

                rev_codon = "".join(complement.get(base,base) for base in rev_codon) # Complement the sequence

                if len(codon) == 3:
                    codons.append(codon)
                    translated_codons.append(translation_table[codon])
                if len(rev_codon) == 3:
                    rev_codons.append(rev_codon)
                    translated_rev_codons.append(translation_table[rev_codon])
         

            print(gene+'-'+f'frame-{frame+1}-codons\n',*codons, '\n'+gene+'-'+f'reverseframe-{frame+1}-codons\n',*rev_codons, sep = ' ', file = nt_file)
            print(gene+'-'+f'frame-{frame+1}-aminos\n',*translated_codons, '\n'+gene+'-'+f'reverseframe-{frame+1}-aminos\n',*translated_rev_codons, sep = ' ', file = tr_file)




