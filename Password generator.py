import random
import string

def generate_password(length=12):
    """Generate a random password of a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
new_password = generate_password()
print("Generated password:", new_password)
