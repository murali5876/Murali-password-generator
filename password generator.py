import random
import string

def generate_password(length=12):
    """
    Generate a random password with a mix of uppercase and lowercase letters,
    numbers, and special characters.
    
    Parameters:
    - length (int): Length of the password. Default is 12.
    
    Returns:
    - str: The generated password.
    """
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Generate the rest of the password
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the characters to make the password more secure
    random.shuffle(password)

    # Convert the list to a string
    password_str = ''.join(password)

    return password_str

def generate_multiple_passwords(num_passwords, length=12):
    """
    Generate multiple random passwords.
    
    Parameters:
    - num_passwords (int): Number of passwords to generate.
    - length (int): Length of each password. Default is 12.
    
    Returns:
    - list: A list of generated passwords.
    """
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    try:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
        
        if length < 4:
            raise ValueError("Password length must be at least 4.")
        
        passwords = generate_multiple_passwords(num_passwords, length)
        
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"{i}. {password}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
