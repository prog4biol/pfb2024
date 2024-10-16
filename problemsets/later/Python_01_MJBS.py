#!/usr/bin/env python3
import sys
	# PYTHON PROBLEM SET 1
#Answers by Majo Blanco

#1.  Start up the Python Interactive Interpreter.
# Print out "Hello New York"
print("Hello New York")

#Store your name in a variable
myname = "Majo Blanco"

# Print the contents of this variable.#
print(myname)




#2.  Working with a text editor. Use vi to write a script. Name your script something like python1.py or me.py . Python scripts should always have the .py extension.
#vi python1.py
#press i
#write !/usr/bin/env python3 at the beginning of the document

name = "Majo Blanco"
Favcolor = "Tile"
FavAnimal = "cats"
FavActivity = "Biking"
nl = '\n'
print(f'My name:{name}{nl}My favorite color:{Favcolor}{nl}My favorite animal: {FavAnimal}{nl}My favorite activity:{FavActivity}')



# 3. Use sys.argv (make sure to import sys!!!) to retrieve your name, favorite color, favorite activity, and favorite animal from the command line. Remember to check out the example in the notes. Print all the variables in one print statement.

usrname = input("Give me user name")
usrcolor = input("What is your favorite color?")
usrAnimal = input("What is your favorite animal")
usrActivity = input("What is your favorite activity?")
print(f'User name: {usrname}{nl}User favorite color: {usrcolor}{nl}User favorite animal: {usrAnimal}{nl}User favorite activity: {usrActivity}')
