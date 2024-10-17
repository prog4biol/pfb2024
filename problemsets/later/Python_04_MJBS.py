#!env/bin/bash python3
# Python 04 problem set Lists and loops
import sys

#1. For the next series of tasks about lists use the interpreter:
	#1.1 Create a list of 5 of your favorite things.
favThings = ["Nature", "Music", "Dancing", "Singing", "Biking"]

	#1.2 Use the print() function to print your list.
print("My original list of favorite things:",favThings)

	#1.3 Use the print() function to print out the middle element
print("Middle favorite thing, method 1:",favThings[2])
print("Middle favorite thing, method 2:",favThings[len(favThings)//2]) # divides the length of the list by two and scales down one if not odd

	#1.4 Now replace the middle element with a different item, your favorite song, or song bird
favThings[len(favThings)//2] = "Mockingjay"

	# 1.5 Use the same print statement from b. to print your new list. Check out the differences.
print("Modified middle favorite thing with bird", favThings)

	#1.6 Add a new element to the end.
favThings.append("sleeping")

	#1.7 Add a new element to the beginning
favThings.insert(0, "Sciencing")

	#1.8 Add a new element somewhere other than the beginning or the end.
favThings.insert(4, "Loving")
print("I just added a bunch of things at the beggining, end and somewhere 4:", favThings)

	#1.9 Remove an element from the end.
favThings.pop()
print("Just used pop to remove something at the end", favThings)

	#1.10 Remove an element from the beginning.
favThings.pop(0)
print("Just used pop to remove something at the start", favThings)

	#1.11 Remove an element from somewhere other than the beginning or the end.
favThings.pop(3)
print("removed something other than start and end", favThings)

	#1.12 Use join to create a string. Join the elements on ', '
s = ", "
print(s.join(favThings))


#2. Write a script with a text editor that splits a string into a list. In your script:

	#2.1 Save the string sapiens, erectus, neanderthalensis as a variable named taxa
taxa = "sapiens, erectus, neanderthalensis"
	
	#2.2 Print taxa
print(taxa)

	#2.3 Print taxa[1], what do you get?
print("Printig taxa[1]", taxa[1])

	#2.4 Print type(taxa). What is it's type?
print("Type of taxa", type(taxa))

	#2.5 Split taxa into individual words and print the result of the split. (Think about the ', '.)
print(taxa.split(s))

	#2.6 Store the result of split in a new variable named species.
species = taxa.split(s)

	#2.7 Print species
print("printing species", species)

	#2.8 Print the species[1], What do you get?
print("Printing species[1]", species[1])

	#2.9 Print type(species). What is it's type?
print("printing type of species", type(species))

	#2.10 Sort the list alphabetically and print (hint: lookup the function sorted()).
print(species.sort(key=str.lower))

	#2.11 Sort the list by length of each string and print. (The shortest string should be first).
sortedList = sorted(species, key=lambda x: len(x))
print("Elements of list sorted into length",sortedList)

#4 Write a script with a text editor that uses a while loop to print out the numbers 1 to 100.
count = 1
while count < 101:
	#print(count)
	count += 1

#5 Write a script that uses a while loop to calculate the factorial of 1000.
num = 1000
factorial_list = [ ]

while num >= 1:
	#print(num)
	factorial_list.append(num)
	num = num - 1

#print(factorial_list)
	
def multiply_list(list):
	factorial = 1
	for x in list:
		factorial = factorial * x
	return factorial
print("The factorial is", multiply_list(factorial_list))

#  Write a script Iterate through each element of this list using a for loop: [101,2,15,22,95,33,2,27,72,15,52]. Print out the values
lista = [101,2,15,22,95,33,2,27,72,15,52]
for elem in lista:
	print("eelement in list",elem)

#7 Add to your previous script: Sort the elements of the above list, then iterate through each element using a for loop and:
srt_lista = sorted(lista)
#print(type(srt_lista))
even_vals = 0
odd_vals = 0

for elem in srt_lista:
	#7.1 Print each element.
	print(elem)
	#7.2 Calculate two cumulative sums, one of all the even values and one of all the odd values.
	if elem%2 == 0:
		even_vals = even_vals + elem
	else:
		odd_vals = odd_vals + elem
	#7.3 Print only the final two sums.

print("even sum", even_vals)
print("odd sum", odd_vals) 

#8 Write a new script that uses range() in a for loop to print out every number between 0 and 99
num = 0
for num in range(0,99):
	print(num)

#9 Create a new script that uses list comprehension to print out every number between 1 and 100.
heregoes = [x for x in range(1,101)]
print(heregoes)

#10 Write a new script that takes the start and end values from the command line (sys.argv). If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.
start_val = int(sys.argv[1])
end_val = int(sys.argv[2])

for x in range(start_val, end_val +1):
	if x%2 ==1:
		print(x)

	#10.1 Modify your script so that it will only print the number if it is odd.

#11 Write a new script to create a list with the following data ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']. Use a for loop to iterate through each element of this list and:
nva = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

	#11.1 Print out each element.
for seq in nva:
	print(seq)
	
	#11.2 Print out the length and the sequence, separated by a tab.
for seq in nva:
	print(len(seq), seq, sep = "\t")
	
	#11.3 Modify this script to also also print out the number (postion in the list) of each sequence. Make sure your columns are tab separated (i.e., "1\t4\tACGT\n")
n = 0
#print(nva[0]) 
for n in range(0, len(nva)):
	#print(n)
	seq = nva[n]
	#print(seq)
	print(len(seq), nva[n], n, sep = "\t")
	n = n + 1

#12 Write a new script tht uses list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence (i.e., "4\tATGC\n"). A list of tuples looks like this [(4,'ATGC'),(2,'GC')].
loft = [(n, nva[n]) for n in range(0, len(nva))]
print(loft)
