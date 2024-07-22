import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random choices from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main function to run the password generator
def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated password of length {length}:")
    print(password)

# Run the main function
if __name__ == "__main__":
    main()
