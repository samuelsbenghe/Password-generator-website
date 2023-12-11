import string
import random

def generate_password(number_of_characters: str, add_numbers: bool, add_symbols: bool):
    characters = list(string.ascii_letters) # ['a', 'b', 'c', ..., 'A', 'B', 'C', ...]
    if add_numbers:
        characters += list(string.digits) # ['a', 'b', 'c', ..., 'A', 'B', 'C', ..., '0', '1', '2', ...]
    if add_symbols:
        characters += list(string.punctuation) # ['a', 'b', 'c', ..., 'A', 'B', 'C', ..., '0', '1', '2', ..., '!', '@', '#', ...]
        
    password = ''
    if number_of_characters > 0:
        for _ in range(number_of_characters):
            password += random.choice(characters)
    else:
        password = 'Invalid number of characters!'
    return password