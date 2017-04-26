import string
import random


vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"

letter_input_1 = input("What letter do you want? Enter 'c' for consonants, 'v' for vowels or 'l' for any letter: ")
letter_input_2 = input("What letter do you want? Enter 'c' for consonants, 'v' for vowels or 'l' for any letter: ")
letter_input_3 = input("What letter do you want? Enter 'c' for consonants, 'v' for vowels or 'l' for any letter: ")


def generate_name():
    if letter_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input_1 == 'c':
        letter1 = random.choice(consonants)
    elif letter_input_1 == 'l':
        letter1 = random.choice(string.ascii_lowercase)
    else:
        letter1 = letter_input_1
    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        letter2 = random.choice(consonants)
    elif letter_input_2 == 'l':
        letter2 = random.choice(string.ascii_lowercase)
    else:
        letter2 = letter_input_2
    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        letter3 = random.choice(consonants)
    elif letter_input_3 == 'l':
        letter3 = random.choice(string.ascii_lowercase)
    else:
        letter3 = letter_input_3
    name = letter1 + letter2 + letter3
    return name

for i in range(10):
    print(generate_name())
