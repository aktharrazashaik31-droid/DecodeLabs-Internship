import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return None

    # Ensure complexity
    password = [
        random.choice(string.ascii_uppercase),  # At least 1 uppercase
        random.choice(string.ascii_lowercase),  # At least 1 lowercase
        random.choice(string.digits),           # At least 1 digit
        random.choice("!@#$%^&*")               # At least 1 special character
    ]

    # Remaining characters
    all_characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*"
    )

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle for randomness
    random.shuffle(password)

    return "".join(password)

# Main Program
print("=== Random Password Generator ===")

try:
    length = int(input("Enter password length: "))

    password = generate_password(length)

    if password:
        print("\nGenerated Password:", password)

except ValueError:
    print("Please enter a valid number.")
