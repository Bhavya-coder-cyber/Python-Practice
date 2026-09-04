import base64
import os

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special_character = any(c in "!@#$%^&*()" for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_special_character])
    return ["weak", "medium", "strong", "very strong"][min(score, 3)]

def add_credentials():
    website = input("Enter the website: ").strip()
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()
    password_score = password_strength(password)

    print(f"Password strength: {password_score}")
    
    text = f"{website}||{username}||{password}"

    with open(VAULT_FILE, "a", encoding="utf-8") as f:
        f.write(encode(text) + "\n")

    print("Credentials added successfully")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("No credentials found")
        return

    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            text = decode(line.strip())
            website, username, password = text.split("||")
            print(f"Website: {website}")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print()

def update_credentials():
    username = input("Enter the username: ").strip()
    

def main():
    while True:
        print("1. Add credentials")
        print("2. View credentials")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_credentials()
        elif choice == "2":
            view_credentials()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()