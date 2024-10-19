#!env/bin/bash python3
import re
# python 8 Data structures problem set

# 1. Take a multi-FASTA Python_08.fasta file from user input and calculate the nucleotide composition for each sequence. 
# #Use a datastructure to keep count. 
# #Print out each sequence name and its compostion in this format seqName\tA_count\tT_count\tG_count\C_count
counter_dict = {}
header_cnt = 0
#i am imagining a structure such as
    #dict = {
        #header1: [seqid, description, sequence, {"a": num, "t": num, "c": num, "g": num}]
        #header2: [seqid, description, sequence, {"a": num, "t": num, "c": num, "g": num}]
    #}
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
                        counter_dict[seqName][1]['A'] = counter_dict[seqName][0].count('A')
                        counter_dict[seqName][1]['T'] = counter_dict[seqName][0].count('T')
                        counter_dict[seqName][1]['C'] = counter_dict[seqName][0].count('C')
                        counter_dict[seqName][1]['G'] = counter_dict[seqName][0].count('G')
                    else:
                         counter_dict[seqName].append(line)
                         counter_dict[seqName].append({'A': line.count('A'), 'T': line.count('T'), 'C': line.count('C'), 'G': line.count('G')})
print(counter_dict)

for key in counter_dict:
    print(f'seqName: {key} \tA_count: {counter_dict[key][1]['A']} \tT_count {counter_dict[key][1]['T']} \tG_count {counter_dict[key][1]['G']}\tC_count {counter_dict[key][1]['C']}')