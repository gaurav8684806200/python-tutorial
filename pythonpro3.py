import random
import string

def generate_password(length):
    if length > 4:
        return "password length should be at least 4 characters"
    

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation


    all_chars = upper + lower + digits + special

    password =  [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(all_chars, k=length)

    random.shuffle(password)

    return ''.join(password)

try:
    length = int(input("enter the desired password length:"))
    print("generated password:", generate_password(length))
except ValueError:
    print("please enter a valid number.")
        