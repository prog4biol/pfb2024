#!env/bin/bash python3
import re
# python 8 Data structures problem set Question 2
# Write a script that takes a multi-FASTA file Python_08.fasta from user input 
# #and breaks each sequence into codons (every three nucleotides is a codon) in just the first reading frame. 
# #Your output should look like this
# seq1-frame-1-codons
# CAT GCT TGA GTC
counter_dict = {}
k = 3
n = 0
with open("Python_08.fasta", "r") as fasta:
    for line in fasta:
        line = line.rstrip()
        line = line.upper()
        if re.findall(r"^[>].*|\s.*", line):
            sep = re.search(r"(^>[^\s]*)|\s(.*)", line)
            seqName = sep.group(1)
            counter_dict[seqName] = []
        else:
             if re.search(r"[ATCG]*", line):
                if seqName in counter_dict:
                    if len(counter_dict[seqName]) > 0:
                        counter_dict[seqName][0] =counter_dict[seqName][0] + line
                        seq = counter_dict[seqName][0]
                        #print(len(counter_dict[seqName][0])-3)
                        #for n in range(n, len(counter_dict[seqName][0]), k): # this sone in theory works for the creation of the three framess
                        counter_dict[seqName][1]["seq-frame-1-codons"].append([seq[i:i+k] for i in range(0, len(seq), k)])
                        #print(counter_dict[seqName][1]["codons"].append(counter_dict[seqName][0][0:3]))
                    else:
                         counter_dict[seqName].append(line)
                         counter_dict[seqName].append({"seq-frame-1-codons": []})
print(counter_dict)