import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            password_length = int(input("Enter the desired length of the password (minimum 8 characters): "))
            if password_length < 8:
                print("Password length should be at least 8 characters. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    generated_password = generate_password(password_length)
    print("\nGenerated Password:", generated_password)

if __name__ == "__main__":
    main()
