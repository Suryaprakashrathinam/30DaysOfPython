import random #Python module to generate random values
import string #Module that contains pre-defined sets of characters (like letters, digits, punctuation).

def generate_password(length): #desired password length
    characters = string.ascii_letters + string.digits + string.punctuation
    #Combines all letters (uppercase + lowercase), digits (0–9), and special characters into one string.
    password = ''.join(random.choice(characters) for i in range (length))
    '''
    random.choice(characters) → Picks one random character from the pool.
    for i in range(length) → Repeats this selection length times.
    ''.join(...) → Joins all randomly chosen characters into a single string (i.e., the password).
    '''
    return password

password_length = 8
new_password = generate_password(password_length)

print(f"Generated password: {new_password}")