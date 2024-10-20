#!/usr/bin/env python3



# 1. Create a DNA sequence class that will contain a sequence, its name, and it's organism of origin. Do this by creating an __init__ function
class DNAsequence(object):

    def __init__(self, sequence, seq_name, species_name):
        self.sequence = sequence
        self.seq_name = seq_name
        self.species_name = species_name

# 2. Write some some lines of code, outside your class (in your main program) that sets the name, DNA sequence, and organism for a gene.

dna_seq_object = DNAsequence('ATGGACTCCCGTAACTTTTGACT', 'Random_Sequence', 'Random_Species')

# 3. Write some some lines of code, outside your class that:

#   a. uses the object sequence attribute to retrieve and print the sequence.
#   b. uses the object name attribute to retrieve and print the name.
#   c. uses the object organism attribute to retrieve and print the organism.

seq = dna_seq_object.sequence
name = dna_seq_object.seq_name
species_name = dna_seq_object.species_name

print(f'Sequence: {seq}\nSequence Name: {name}\nSpecies Name: {species_name}')








