#Q1
import csv
import os

# INPUT_FILE = 'students.csv'
# OUTPUT_FILE = 'students_output.csv'

# def open_csv_file():
#     if not os.path.exists(INPUT_FILE):
#         print(f"Error: The file '{INPUT_FILE}' does not exist.")
#         return None
#     try:
#         with open(INPUT_FILE, 'r', newline='') as f:
#             reader = csv.DictReader(f)
#             output_data = []
#             data = list(reader)
#             for row in data:
#                 total_marks = int(row['python']) + int(row['maths']) + int(row['statistics'])
#                 average = round(total_marks/3, 2)
#                 print(f"Name: {row['name']}, Python: {row['python']}, Maths: {row['maths']}, Statistics: {row['statistics']}, Total: {total_marks}, Average: {average}")
#                 output_data.append({'Name': row['name'], 'Total': total_marks, 'Average': average})
#             write_csv_file(output_data)
#     except:
#         print(f"Error: An error occurred while opening the file '{INPUT_FILE}'.")
#         return None

# def write_csv_file(data):
#     if data is None:
#         return
#     try:
#         with open(OUTPUT_FILE, 'w', newline="", encoding='utf-8') as f:
#             writer = csv.DictWriter(f, fieldnames=['Name', 'Total', 'Average'])
#             writer.writeheader()
#             writer.writerows(data)
#         print(f"Data has been written to '{OUTPUT_FILE}'.")
#     except:
#         pass

# def get_max_marks():
#     max_marks = 0
#     with open(OUTPUT_FILE, 'r', newline='') as f:
#         max_marks = max(csv.DictReader(f), key=lambda x: x['Total'])
#     print(f"Maximum marks: {max_marks['Name']}, Total: {max_marks['Total']}, Average: {max_marks['Average']}")

# if __name__ == "__main__":
#     open_csv_file()
#     get_max_marks()

#Q2
import json

# SETTINGS_FILE = 'settings.json'

# def load_settings():
#     if not os.path.exists(SETTINGS_FILE):
#         return {}
#     try:
#         with open(SETTINGS_FILE, 'r') as f:
#             return json.load(f)
#     except:
#         return {}

# def save_settings(data):
#     with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=2)

# def add_settings():
#     settings = load_settings()
#     settings['username'] = input("Enter username: ")
#     settings['theme'] = input("Enter theme: ")
#     settings['language'] = input("Enter language: ")
#     save_settings(settings)

# def edit_settings():
#     settings = load_settings()
#     field = input("Enter the field to edit: ")
#     field_map = {
#         "username": "username",
#         "theme": "theme",
#         "language": "language"
#     }
#     if field not in field_map:
#         print("Invalid field")
#         return
#     new_value = input("Enter the new value: ")
#     settings[field] = new_value
#     save_settings(settings)

# def display_settings():
#     settings = load_settings()
#     print("Settings:")
#     print(f"Username: {settings.get('username', 'Not found')}")
#     print(f"Theme: {settings.get('theme', 'Not found')}")
#     print(f"Language: {settings.get('language', 'Not found')}")

# def main():
#     while True:
#         print("1. Add settings")
#         print("2. Edit settings")
#         print("3. Display settings")
#         print("4. Exit")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             add_settings()
#         elif choice == "2":
#             edit_settings()
#         elif choice == "3":
#             display_settings()
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice")

# if __name__ == "__main__":
#     main()

#Q3
import requests
import matplotlib.pyplot as plt

# EXPENSE_FILE = 'daily_expenses.csv'

# def load_expenses():
#     categories = []
#     expenses = [] 
#     if not os.path.exists(EXPENSE_FILE):
#         return
#     try:
#         with open(EXPENSE_FILE, 'r', newline='') as f:
#             reader = csv.DictReader(f)
#             data = list(reader)
#             for row in data:
#                 if row['category'] not in categories:
#                     categories.append(row['category'])
#                     expenses.append(int(row['amount']))
#                 else:
#                     index = categories.index(row['category'])
#                     expenses[index] += int(row['amount'])
#     except:
#         pass
#     return categories, expenses

# if __name__ == "__main__":
#     categories, expenses = load_expenses()
#     print(categories)
#     print(expenses)

#     plt.figure(figsize=(10, 6))
#     plt.bar(categories, expenses, color='blue')
#     plt.title('Daily Expenses')
#     plt.xlabel('Category')
#     plt.ylabel('Amount')
#     plt.savefig('daily_expenses.png')
#     plt.show()

#Q4
from cryptography.fernet import Fernet

# VAULT_FILE = 'msg_vault.txt'
# KEY_FILE = 'new_vault.key'

# def load_or_create_key():
#     if not os.path.exists(KEY_FILE):
#         key = Fernet.generate_key()
#         with open(KEY_FILE, "wb") as f:
#             f.write(key)
#     else:
#         with open(KEY_FILE, "rb") as f:
#             key = f.read()
#     return Fernet(key)

# fernet = load_or_create_key()
# def encrypt(message):
#     encodedMessage = fernet.encrypt(message.encode()).decode()
#     with open(VAULT_FILE, "w", encoding="utf-8") as f:
#         f.write(encodedMessage)

#     print("Message encrypted and saved to", VAULT_FILE)

# def decrypt():
#     with open(VAULT_FILE, "r", encoding="utf-8") as f:
#         encodedMessage = f.read()
#     decode = fernet.decrypt(encodedMessage.encode()).decode()
#     print(decode)

# if __name__ == "__main__":
#     message = input("Enter the message: ").strip()
#     encrypt(message)
#     decrypt()

#Q5

    