#!env/bin/bash python3
import re

#1 .In the file Python_07_nobody.txt find every occurrence of 'Nobody' and print out the position.
with open("Python_07_nobody.txt","r") as nobody:
	for line in nobody:
		for Nanay in  re.finditer(r"(Nobody)", line):
			whole = Nanay.group(0)
			start = Nanay.start(1) + 1
			end = Nanay.end(1)
			print(whole, start, end, sep = "\t")

# 2. In the file Python_07_nobody.txt substitute every occurrence of 'Nobody' with your favorite name and write an output file with that person's name (ex. Michael.txt).
Sean = open("Sean.txt","w")
with open("Python_07_nobody.txt", "r") as nobody:
	for line in nobody:
		line = line.rstrip()
		for Nanay in re.finditer(r"(Nobody)", line):
			start = Nanay.start(1) + 1
			end = Nanay.end(1)
			line_sean = line[0:start-1] + "Sean" + line[end:len(line)]
			print(line_sean)
			Sean.write(line_sean + "\n")
Sean.close()


#3 .Using pattern matching, find all the FASTA header lines in Python_07.fasta. Note that the format for a header in a FASTA file is a line that starts with a greater than symbol and is followed by some text (e.g. >seqName description where seqName is the sequence name or identifier. The identifier cannot have spaces in it. The description that follows it can have spaces.)
Headers = []
with open("Python_07.fasta","r") as fasta:
	for line in fasta:
		line = line.rstrip()
		if re.findall(r"^[>].*|\s.*", line):
			Headers.append(line)
print(Headers)

# 4 If a line matches the format of a FASTA header, extract the sequence name and description using sub patterns (groups).
# Print sequence information in this format: id:seqName desc:seqDescription
for header in Headers:
	sep = re.search(r"(^>[^\s]*)\s(.*)", header)
	idseq = sep.group(1)
	desc = sep.group(2)
	print(f"id: {idseq} desc: {desc}")


# Create a FASTA parser, or modify your FASTA parser from the previous problem set, to use regular expressions. Also make sure your parser can deal with a sequence that is split over many lines.
di = {}
with open("fasta_file.fasta", "r") as fasta_p:
	for line in fasta_p:
		line = line.rstrip()
		line = line.upper()
		if re.findall(r"^[>].*|\s.*", line):
			sep = re.search(r"(^>[^\s]*)|\s(.*)", line)
			idseq = sep.group(1)
			desc = sep.group(2)
			di[idseq] = [idseq, desc]
		else:
			di[idseq].append(line)

print(di)



