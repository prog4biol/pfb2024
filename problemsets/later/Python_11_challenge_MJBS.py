##!env/bin/bash python3
import re
# python 11 Classes problem set
# Challenge question
#Create a method that can compare two DNA Sequence records and returns True if they are the same or False if they are differet. 
# #Sameness is based on name, organism, and seqeunce. All need to be the same for two objects to be considered the same.

## HERE I DEFINE CLASSES ##
#defining a class DNAsequence
class DNAsequencecomparison(object):
    #1 define class atributes
    def __init__(self,sequence1,name1,organism1,sequence2, name2, organism2):
        self.sequence1 = sequence1
        self.genename1 = name1
        self.origin1 = organism1
        self.sequence2 = sequence2
        self.genename2 = name2
        self.origin2 = organism2
    # creating a method to create a dictionary with atributes1
    def Createdict(self):
        dictofattr1 = {}
        header1 = self.genename1 + self.origin1
        dictofattr1[header1] = self.sequence1
        #print(dictofattr1)
        return dictofattr1
    #creating a method to query on said dictionary with atributes2
    def Queryindict(self):
        dictofattr1 = self.Createdict()
        header2 = self.genename2 + self.origin2
        if header2 in dictofattr1:
            if dictofattr1[header2] == self.sequence2:
                isitequal = True
            else:
                isitequal = False
        else:
            isitequal = False
        return isitequal
    

## This is my main program ##
dna_object = DNAsequencecomparison('AAAAAAATTCCGG','gene1','Danio Rerio','AAATTCCGG','gene1','Droso')
print(f"Are my sequences {dna_object.sequence1} and {dna_object.sequence2}, with gene names \"{dna_object.genename1}\" and \"{dna_object.genename2}\", of organisms \"{dna_object.origin1}\" and \"{dna_object.origin2}\" equal?", dna_object.Queryindict())
