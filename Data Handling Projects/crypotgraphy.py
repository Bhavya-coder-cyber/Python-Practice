import os
import json
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
            
    return Fernet(key)
    
fernet = load_or_create_key()

def load_file():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def write_file(data):
    with open(VAULT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_note():
    title = input("Enter the title: ").strip()
    content = input("Enter the content: ").strip()

    encrypted_content = fernet.encrypt(content.encode()).decode()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_file()

    data.append({
        "title": title,
        "content": encrypted_content,
        "timestamp": timestamp
    })
    write_file(data)
    print("Data saved successfully")

def list_notes():
    data = load_file()
    if not data:
        print("No data is present")
        return

    for i, note in enumerate(data, 1):
        print(f"{i}. {note["title"]} {note["timestamp"]}")

def view_notes():
    index = int(input("Enter the index number: ")) - 1
    data = load_file()

    try:
        if 0 <= index <= len(data):
            encrypted_content = data[index]["content"]
            decrypted_content = fernet.decrypt(encrypted_content.encode()).decode()
            print(f"\n 📝 {data[index]["title"]} - {data[index]["timestamp"]} \n\n {decrypted_content}")
        else:
            print("Invalid Index")
    except ValueError:
        print("Invalid Input")

def search_notes():
    keyword = input("Enter the keyword to search in notes: ").strip().lower()
    data = load_file()
    found = (note for note in data if keyword in note["title"].lower())
    if not found:
        print("Not found in the notes")
    else:
        for note in found:
            print(f"{note["title"]} - {note["timestamp"]}")

def main():
    while True:
        print(f"\n Offline Notes Locker")
        print("1. Add Notes")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        match choice:
            case "1": add_note()
            case "2": list_notes()
            case "3": view_notes()
            case "4": search_notes()
            case "5": break
            case _: print("Invalid Input")

if __name__ == "__main__":
    main()