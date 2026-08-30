import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])


def add_contacts():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    with open(FILENAME, "r", encoding="utf-8") as f:
        rows = csv.DictReader(f)

        for row in rows:
            if row["Phone"] == phone:
                print("Contact already exists")
                return

    with open(FILENAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])

    print("Contact added successfully")


def view_contacts():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) <= 1:
            print("No contacts found")
            return

        for row in rows[1:]:
            if not row:
                continue
            print(f"{row[0]} | {row[1]} | {row[2]}")

        print()


def search_contacts():
    term = input("Enter the name to search: ").strip().lower()
    found = False

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if term in row["Name"].lower():
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                found = True

    if not found:
        print("Contact not found")

def update_contacts(name):
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        found = False
        for row in rows:
            if name.lower() in row["Name"].lower():
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                edit_field = input("Enter the feild to edit: ").strip().lower()
                field_map = {
                    "name": "Name",
                    "phone": "Phone",
                    "email": "Email"
                }

                if edit_field not in field_map:
                    print("Invalid field")
                    return

                new_value = input("Enter the new value: ").strip()
                row[field_map[edit_field]] = new_value
                found = True
                print("Contact updated successfully")
                break
    if not found:
        print("Contact not found")
        return
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email"])
        writer.writeheader()
        writer.writerows(rows)

def delete_contacts(name):
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        found = False
        updated_rows = []
        for row in rows:
            if name.lower() in row["Name"].lower():
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                found = True
            else:
                updated_rows.append(row)
    if not found:
        print("Contact not found")
        return
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email"])
        writer.writeheader()
        writer.writerows(updated_rows)
    print("Contact deleted successfully")

def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contacts()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contacts()

        elif choice == "4":
            name = input("Enter the name of the contact to update: ").strip().lower()
            update_contacts(name)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ").strip().lower()
            delete_contacts(name)
        
        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()