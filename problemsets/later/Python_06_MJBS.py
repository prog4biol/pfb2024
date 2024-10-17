#!env/bin/bash python3

# 1, Make a set using the two different syntaxes for creating a set myset = set() and myset2 = {}.
mySet = set('ATGTGGG')
mySet2 = {'ATGTGGG'}

#1.1 What is the difference?
#print(mySet)
#print(mySet2)
#1.2 Does it matter which method you use? Yes
#1.3 How many items are in mySet and mySet2? mySet has 3 items, while mySet2 has only one

#2. Write a script that creates 2 sets using the collections of numbers below. Find the intersection, difference, union, and symetrical difference between these two sets.
set1 = {3, 14, 15, 9, 26, 5, 35, 9}
set2 = {60, 22, 14, 0, 9}
print("My set 1: ",set1)
print("My set2: ", set2)

#2.1 intersection
print("Intersection ", set1&set2)
#2.2 difference
print("difference ", set1-set2)
#2.3 union
print("union ", set1|set2)
#2.4 symetrical difference
print("Symmetrical difference ", set1^set2)

#3. If you create a set using a DNA sequence, what will you get back? Try it with this sequence:
setDNA = {'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTNNGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACX'}
print(setDNA)

#4. Nucleotide Composition. Write a script that:
# 4.1 determines the unique characters in this sequence
DNA = 'GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA'
unoqdict = {}
set_uniq_DNA = set(DNA)
print("set(DNA) ", set_uniq_DNA)

#4.2 iterate over each unique character and count the number found in the sequence
for nt in set_uniq_DNA:
	unoqdict[nt] = DNA.count(nt)
# store each count in a dictionary. example: nt_comp['A']=2
#when you are done counting each character calculate and report the nucleotide composition and the GC content.
print("Nucleotide composition: ", unoqdict)
print("GC content", unoqdict['G']+unoqdict['C']/len(DNA))

#5 . Write a script to do the following to Python_06.txt
#5.1 Open and read the contents.
file_txt = open('Python_06.txt', 'r')
#5.2 Uppercase each line
for line in file_txt:
	nline = line.rstrip()
	print(nline.upper())
#5.3 Print each line to the STDOUT
file_txt.close()

# 6. Modifiy the script in the previous problem to write the contents to a new file called "Python_06_uc.txt"
with open("Python_06.txt", "r") as file_txt:
	output = open("Python_06_uc.txt","w")
	for line in file_txt:
		nline = line.strip()
		output.write(nline.upper() + "\n")

	output.close()

# 7 Open and print the reverse complement of each sequence in Python_06.seq.txt. Each line is the following format: seqName\tsequence\n. Make sure to print the output in FASTA format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'.
nl = "\n"
with open("Python_06.seq.txt","r") as seq_txt:
	for line in seq_txt:
		complement_seq = ''
		nline = line.rstrip()
		nline = nline.upper()
		seqName, Sequence = nline.split('\t')
		count = 0 
		for count in range(0, len(Sequence)):
			if Sequence[count] == 'A':
				complement_seq = complement_seq + 'T'
			elif Sequence[count] == 'T':
				complement_seq = complement_seq + 'A'
			elif Sequence[count] == 'C':
				complement_seq = complement_seq + 'G'
			else:
				complement_seq = complement_seq + 'C'
			count = count + 1
		reverse_complement = complement_seq[::-1]
		#print(f'>{seqName} Reverse complement{nl}{reverse_complement}')

# 8 Open the FASTQ file Python_06.fastq and go through each line of the file. Count the number of lines and the number of characters per line. Have your program report the:
# total number of lines
#total number of characters 
# average line length
count_line = 0
count_char = 0
line_lengths = []
with open("Python_06.fastq", "r") as fastq:
	for line in fastq:
		count_line = count_line + 1
		for char in line:
			count_char = count_char + 1
		line_lengths.append(len(line))
average_line_length = sum(line_lengths)/len(line_lengths)
print(f'The total number of lines is: {count_line}, the total number of characters is: {count_char}, and the average line length: {average_line_length}')


#9 Write your first FASTA parser script. This is a script that reads in a FASTA file and stores each FASTA record separately for easy access for future analysis.
#Open your file
#read each line
#is your line a header line? is it a sequence line?
#does a single FASTA record have one line of sequence or multiple lines of sequence?
# at the end return dict
milista = []
directorio = {}
counter_key = ""
with open("fasta_file.fasta", "r") as fasta:
	for line in fasta:
		nline = line.rstrip()
		nline = nline.upper()
		print(nline)
		#I can create a list of tuples, where each touple has the header and sequence pair of the fasta
		# THEN I CAN convert the list into the dict?
		#separate by ">" first and the separate by \n
		if nline[0] == ">":
			counter_key = nline[1:len(nline)]
			directorio[counter_key] = ""
		else:
			directorio[counter_key] = nline

print(directorio)		
#temp = iter(fasta.split(">"))
#res = [(ele, next(temp)) for ele in temp]
#print(res)

