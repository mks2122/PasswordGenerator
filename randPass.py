import random
import string
import pyperclip


def generate_password(length=16):
    # Define the rules for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all the rules into one string
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a password with random characters
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# # Generate a password with default length of 8 characters
# password = generate_password()
# pyperclip.copy(password)

# print(password)
