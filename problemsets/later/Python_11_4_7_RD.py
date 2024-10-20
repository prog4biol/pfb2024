#!/usr/bin/env python3


'''
4. - 7.

4. Sequence length method
a. Add a method to your class that caclulates and returns the length of the sequence.
b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence length using your new method

5. Nucleotide composition method
a. Add in a method that caclulates and returns the nucleotide composition.
b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence nucleotide compositio using your new method

6. GC content method
a. Add in a method that caclulates and returns the GC content.
b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence GC content using your new method

7. FASTA Formatter method
a. Add in a method that returns the sequence record in FASTA format.
b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence in FASTA format using your new method

        Challenge Question

1. Create a method that can compare two DNA Sequence records and returns True if they are the same or False if they are differet. Sameness is based on name, organism, and seqeunce. All need to be the same for two objects to be considered the same
'''
class DNAsequence(object):

    def __init__(self, sequence, seq_name, species_name):
        self.sequence = sequence
        self.seq_name = seq_name
        self.species_name = species_name

    # 4.a
    def get_seq_length(self):
        return len(self.sequence)

    # 5.a
    def get_nucl_composition(self):
        A_count = self.sequence.count('A')
        T_count = self.sequence.count('T')
        C_count = self.sequence.count('C')
        G_count = self.sequence.count('G')
        return A_count, T_count, C_count, G_count

    def get_GC_content(self):
        A,G,C,T = self.get_nucl_composition()
        GC_count = G+C
        GC_content = GC_count/sum([A,G,C,T]) * 100
        return GC_count, GC_content

    def fasta_formatter(self):
        fasta_sequence="".join(self.sequence[i:i+60] + '\n' for i in range(0,len(self.sequence),60))  # Adds a newline character every 60 nucleotides  
        return '>{}\n{}'.format(self.seq_name,fasta_sequence)
  
    def __eq__(self,other):
        return self.sequence == other.sequence and self.seq_name == other.seq_name and self.species_name == other.species_name

dna = DNAsequence('AAGTGGGGGGCCTAATGTCTAAAAAAAAAAAAAGGGGGCCCCCCCCCCCCCCCGGGGGGGGGTTTATGTGCCCAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'Cool Sequence', 'Cool Species')

# 4.b
print('Length of sequence:', dna.get_seq_length())


# 5.b
As, Ts, Cs, Gs = dna.get_nucl_composition()
print(f"Number of A's: {As}\nNumber of T's: {Ts}\nNumber of G's: {Gs}\nNumber of C's: {Cs}")

# 6.b

GC_count, GC_content = dna.get_GC_content()
print(f"The GC count for {dna.seq_name} is: {GC_count}\nGC content for {dna.seq_name}: {GC_content:.2f}%")

# 7.b
print(dna.fasta_formatter())

# Challenge question

dna2 = DNAsequence('AAAGTC', 'Uncool Sequence', 'Kinda Cool Species')
dna3 = DNAsequence('AAGTGGGGGGCCTAATGTCTAAAAAAAAAAAAAGGGGGCCCCCCCCCCCCCCCGGGGGGGGGTTTATGTGCCCAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'Cool Sequence', 'Cool Species')

print(dna == dna2)
print(dna == dna3)

