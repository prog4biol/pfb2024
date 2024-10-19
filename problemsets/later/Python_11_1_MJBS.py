##!env/bin/bash python3
import re
# python 11 Classes problem set
# Problem 1, 2, 3, 4, 5, 6, 7
# 1. Create a DNA sequence class that will contain a sequence, its name, and it's organism of origin. Do this by creating an __init__ function.

## HERE I DEFINE CLASSES ##
#defining a class DNAsequence
class DNAsequence(object):
    #1 define class atributes
    def __init__(self,sequence,name,organism):
        self.sequence = sequence
        self.genename = name
        self.origin = organism
# 4 Sequence length method
# 4a. Add a method to your class that caclulates and returns the length of the sequence.
    def Seq_length(self):
        length_seq = len(self.sequence)
        return length_seq
#5 Nucleotide composition method
# 5a. Add in a method that caclulates and returns the nucleotide composition.
    def Nucleotide_composition(self):
        sequp = self.sequence.upper()
        length_seq = self.Seq_length()
        composition_A = sequp.count('A')/ length_seq
        composition_T = sequp.count('T')/ length_seq
        composition_C = sequp.count('C')/length_seq
        composition_G = sequp.count('G')/length_seq
        return [composition_A, composition_C, composition_G, composition_T]
# 6 GC content method
# 6a. Add in a method that caclulates and returns the GC content.
    def GCcontent(self):
        list_of_composition = self.Nucleotide_composition()
        compoC = list_of_composition[1]
        compoG = list_of_composition[2]
        gc_content = (compoC + compoG)/self.Seq_length()
        return gc_content
# 7 FASTA Formatter method
# 7a. Add in a method that returns the sequence record in FASTA format.
    def Fasta_Formatter(self):
        sequp = self.sequence.upper()
        header = ">" + self.genename + " " +self.origin
        sequence = sequp
        return {header:sequence}

## THIS IS MY MAIN PROGRAM ###
# 2. Write some some lines of code, outside your class (in your main program) that sets the name, DNA sequence, and organism for a gene.
dna_record_object = DNAsequence('AAAAAAATTCCGG','gene1','Danio Rerio')
# 3a. uses the object sequence attribute to retrieve and print the sequence.
print("sequence:",dna_record_object.sequence)
# 3b. uses the object name attribute to retrieve and print the name.
print("Gene name:",dna_record_object.genename)
# 3c. uses the object organism attribute to retrieve and print the organism.
print("Organism:",dna_record_object.origin)
#4b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence length using your new method.
print("Length of sequence", dna_record_object.Seq_length())
# 5b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence nucleotide compositio using your new method.
list_nuc_composition = dna_record_object.Nucleotide_composition()
list_to_print = ['A', 'C', 'G', 'T']
i = 0
while i < len(list_nuc_composition):
    print(f'Nucleotide composition of {list_to_print[i]} is: {list_nuc_composition}')
    i += 1
# 6b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence GC content using your new method.
print("The GC content of this gene is: ", dna_record_object.GCcontent())
# 7b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence in FASTA format using your new method.
dict_fasta = dna_record_object.Fasta_Formatter()
for key in dict_fasta:
    print(key)
    print(dict_fasta[key])