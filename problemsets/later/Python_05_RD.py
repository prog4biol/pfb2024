#!/usr/bin/env python3

# 1. Write a script in which you construct a dictionary of your favorite things.
fav_dict = {'book': 'The Summoner Series', 'song': 'Coldplay - Sparks', 'video_game': 'Skyrim', 'sport': 'MMA'}


# 2. Print out your favorite book.

print(fav_dict['book'])

# 3. Print out your favorite book but use a variable in the key.

fav_thing = 'book'
print(fav_dict[fav_thing])

# 4. Now print your favorite tree.
# I don't have a fav tree so heres my fav videogame

print(fav_dict['video_game'])

# 5. Add your favorite 'organism' to the dictionary. Make organism the new key of fav_thing

fav_dict['organism'] = 'Xenopus'

# 6. Use a for loop to print out each key and value of the dictionary.

for i in fav_dict:
    print(i,fav_dict[i], sep = ': ')

# 7 and 8. Take a value from the command line for fav_thing and print the value of that item from the dictionary.
import sys

newline = '\n'
print(f'Pick a favorite thing from these: \n{newline.join(f"{key}" for key in fav_dict)}') 
fav_input = input()
print(f'Robs favorite {fav_input}',fav_dict[fav_input],sep = ': ')

# 9 Change the value of your favorite organism.

fav_dict['organism'] = 'Drosophila'

# 10 Get the fav_thing from the command line and a new value for that key. Change the value with the user inputted value and print out a confirmation

new_organism = input('Pick a new organism: ')
fav_dict['organism'] = new_organism
print('This is the new favorite organism', fav_dict['organism'],sep = ': ' )


