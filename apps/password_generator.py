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
    characters = list_of_characters() # ['a', 'b', 'c', ..., 'A', 'B', 'C', ...]
    if add_numbers:
        characters += list_of_numbers() # ['a', 'b', 'c', ..., 'A', 'B', 'C', ..., '0', '1', '2', ...]
    if add_symbols:
        characters += list_of_symbols() # ['a', 'b', 'c', ..., 'A', 'B', 'C', ..., '0', '1', '2', ..., '!', '@', '#', ...]
        
    password = ''
    if number_of_characters > 0:
        for _ in range(number_of_characters):
            password += random.choice(characters)
    else:
        password = 'Invalid number of characters!'
    return password

# Generate a memorable password
def generate_memorable_password(number_of_characters: int, add_numbers: bool, add_symbols: bool):
    password_parts = list_of_words() # ['apple', 'banana', 'cherry', ...]
    if add_numbers:
        password_parts += list_of_numbers() # ['a', 'b', 'c', ..., 'A', 'B', 'C', ..., '0', '1', '2', ...]
    if add_symbols:
        password_parts += list_of_symbols() # ['a', 'b', 'c', ..., 'A', 'B', 'C', ..., '0', '1', '2', ..., '!', '@', '#', ...]
    password = ''

    # if length of password is less than needed amount of characters, add a random word
    while len(password) < number_of_characters:
        password += random.choice(password_parts) # This will add a random word to the password (it will be bigger than number_of_characters)

    # password is bigger than needed amount of characters, so remove last letter until it is the correct length
    while len(password) > number_of_characters:
        password = password[:-1]
    
    return password

def list_of_words():
    word_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Imbe', 'Jackfruit', 'Kiwi', 'Lime', 'Mango', 'Nectarine', 'Orange', 'Papaya', 'Quince', 'Raspberry', 'Strawberry', 'Tangerine', 'Ugli', 'Vanilla', 'Watermelon', 'Xigua', 'Yuzu', 'Zucchini']
    return word_list

def list_of_characters():
    character_list = list(string.ascii_letters)
    return character_list

def list_of_numbers():
    number_list = list(string.digits)
    return number_list

def list_of_symbols():
    symbol_list = list(string.punctuation)
    return symbol_list