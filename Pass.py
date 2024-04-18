import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("Let's create some strong passwords.")
    
    # Get user input for password length and number of passwords
    length = int(input("Enter the length of the password: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate passwords
    passwords = [generate_password(length) for _ in range(num_passwords)]

    # Print generated passwords
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()
