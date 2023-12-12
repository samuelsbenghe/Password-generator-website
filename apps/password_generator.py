import string
import random

# Main entry point to the password generator
def generate_password(number_of_characters: int, is_memorable:bool, add_numbers: bool, add_symbols: bool):
    if is_memorable:
        return generate_memorable_password(number_of_characters=number_of_characters, add_numbers=add_numbers, add_symbols=add_symbols)
    else:
        return generate_random_password(number_of_characters=number_of_characters, add_numbers=add_numbers, add_symbols=add_symbols)

# Generate a random password
def generate_random_password(number_of_characters: int, add_numbers: bool, add_symbols: bool):
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

# Generate a memorable password
def generate_memorable_password(number_of_characters: int, add_numbers: bool, add_symbols: bool):
    words = return_all_words()
    password = ''
    while len(password) < number_of_characters:
        password += random.choice(words)
    return password

def return_all_words():
    word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'imbe', 'jackfruit', 'kiwi', 'lime', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla', 'watermelon', 'xigua', 'yuzu', 'zucchini']
    return word_list