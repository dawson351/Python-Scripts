# Random password generator
# Brandon Dawson
# 02/06/2024

import random
import string

def generate_password(length=8):
    # Define the usable characters
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all characters
    valid_characters = uppercase_letters + lowercase_letters + digits + special_characters
    
    # Set the minimum length for the password(change based on password length policy)
    length = max(length, 8)
    
    # Generate the password
    password = ''.join(random.choice(valid_characters) for i in range(length))
    
    return password

# Generate a password with 8 characters
password = generate_password()
print("Temporary Password: ", password)