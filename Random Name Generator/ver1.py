import string
import random


def generate_name():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)

    name = letter1 + letter2 + letter3
    return name

print(generate_name())

