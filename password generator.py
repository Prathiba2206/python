import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    # Define character pools
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    # Ensure the character pool is not empty
    if not character_pool:
        raise ValueError("At least one character type must be selected")

    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password
def get_user_preferences():
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    return length, use_uppercase, use_lowercase, use_digits, use_special
def main():
    print("Welcome to the Password Generator!")
    length, use_uppercase, use_lowercase, use_digits, use_special = get_user_preferences()
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
