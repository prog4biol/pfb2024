#!/usr/bin/env python3

#Create a DNA sequence class that will contain a sequence, its name, 
# and it's organism of origin. Do this by creating an __init__ function.

class DNAseq(object):
    def __init__(self, species_name, seq_name, sequence):
        self.species_name=species_name
        self.seq_name=seq_name
        self.sequence=sequence

    #Sequence length method
    def seq_length(self):
        sequence_length=len(self.sequence)
        return(sequence_length)

    #nucleotide composition
    def nt_composition(self):
        # dictionary to store nt
        new_dict={}
        for nt in self.sequence:
            if nt in new_dict:
                new_dict[nt]+=1
            else:
                new_dict[nt]=1
        return(new_dict)
    
    #GC content method
    def GC_content(self):
        nt_dict = self.nt_composition()
        total_nts=sum(nt_dict.values())
        GC_count=sum(list(map(nt_dict.get, ["C", "G"])))
        perc_GC_content=GC_count/total_nts
        return(perc_GC_content)


    #FASTA Formatter method
    # a. Add in a method that returns the sequence record in FASTA format.
    # b. Write some some lines of code, outside your class (in your main program) 
    # that gets and prints the sequence in FASTA format using your new method.

    def make_FASTA_format(self):
        fasta_format=f">{self.seq_name}|{self.species_name}\n{self.sequence}\n"
        return(fasta_format)
    
        
        


#Write some some lines of code, outside your class 
# (in your main program) that sets the name, 
# DNA sequence, and organism for a gene.

organism='salamander'
seq_ID='unknown_gene_1'
DNA_sequence='ATGGGCGGGTATATATATAGGTA'

#Write some some lines of code, outside your class that:
#a. uses the object sequence attribute to retrieve and print the sequence.
#b. uses the object name attribute to retrieve and print the name.
#c. uses the object organism attribute to retrieve and print the organism.

#variables have to be called on in the same order as defined
my_dna_seq_obj=DNAseq(organism,seq_ID,DNA_sequence)

print(f'\tThis is the organism: {my_dna_seq_obj.species_name}\n\
        This is the name of the sequence: {my_dna_seq_obj.seq_name}\n\
        This is the actual sequence: {my_dna_seq_obj.sequence}')

print(f'This is the length of the sequence: {my_dna_seq_obj.seq_length()}')

print(my_dna_seq_obj.nt_composition())

print(my_dna_seq_obj.GC_content())

print(my_dna_seq_obj.make_FASTA_format())


#compares two sequences
#variables must be added as list
class SeqCompare(object):
    def __init__(self, sequence_info1, sequence_info2):
        self.seq1=sequence_info1
        self.seq2=sequence_info2

    def compare_sequences(self):
        successful_hits=0
        #print(self.seq1,self.seq2)
        for item in self.seq1:
            if item in self.seq2:
                #print(item)
                successful_hits+=1
        if len(self.seq1)==successful_hits:
            answer='these are the same'
        else:
            answer='not the same'
        return(answer)
    
seq1_input=[organism,seq_ID,DNA_sequence]
seq2_input=[organism,seq_ID,DNA_sequence]
seq3_input=['cavefish',seq_ID,DNA_sequence]

seq1_vs_seq2 = SeqCompare(seq1_input,seq2_input)
print(seq1_vs_seq2.compare_sequences())

seq1_vs_seq3 = SeqCompare(seq1_input,seq3_input)
print(seq1_vs_seq3.compare_sequences())