import random
import string

def generate_username(name):
    # Generate a username based on the provided name
    username = name.lower().replace(" ", "_")
    return username

def generate_password(length=8):
    # Generate a random password of the specified length
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password