#Q1
import os
from datetime import datetime
from pathlib import Path

# folder_path = input("Enter the folder path: ").strip() or os.getcwd()


# folder = Path(r"C:\Users\jainb\OneDrive\Desktop\Py")
# target_dir = folder / folder_path

# if not target_dir.exists():
#     print(f"The folder path '{folder_path}' does not exist.")
# else:
#     try:
#         files = [items for items in target_dir.iterdir() if items.is_file()]
#         directories = [items for items in target_dir.iterdir() if items.is_dir()]
#         print(f"Total Files: {len(files)}")
#         print(f"Total Directories: {len(directories)}")
#         if files:
#             for file in files:
#                 print(f"File: {file.name}")
#                 print(f"File Size: {round(file.stat().st_size / 1024, 2)} Kb")
#                 modified_timestamp = file.stat().st_mtime
#                 modified_date = datetime.fromtimestamp(modified_timestamp).strftime("%Y-%m-%d %H:%M:%S")
#                 print(f"File Updation Date: {modified_date}")
#             largest_file = max(files, key=lambda f: f.stat().st_size)
#             print(f"Largest File: {largest_file.name}: {round(largest_file.stat().st_size / 1024)} Kb")
#     except:
#         print("File/Folder is not accessible")

#Q2
import random
import time

# questions = [
#     {
#         "question": "What is the output of len([10, 20, 30])?",
#         "options": ["2", "3", "4", "30"],
#         "answer": "3"
#     },
#     {
#         "question": "Which data type stores unique elements?",
#         "options": ["List", "Tuple", "Set", "Dictionary"],
#         "answer": "Set"
#     },
#     {
#         "question": "What does range(2, 6) generate?",
#         "options": [
#             "[2, 3, 4, 5]",
#             "[2, 3, 4, 5, 6]",
#             "[1, 2, 3, 4, 5]",
#             "[3, 4, 5, 6]"
#         ],
#         "answer": "[2, 3, 4, 5]"
#     },
#     {
#         "question": "Which module provides date and time functionality?",
#         "options": ["random", "datetime", "os", "string"],
#         "answer": "datetime"
#     },
#     {
#         "question": "What does the append() method do to a list?",
#         "options": [
#             "Removes the last element",
#             "Adds an element to the end",
#             "Sorts the list",
#             "Clears the list"
#         ],
#         "answer": "Adds an element to the end"
#     },
#     {
#         "question": "Which keyword is used to handle exceptions?",
#         "options": ["catch", "error", "except", "final"],
#         "answer": "except"
#     },
#     {
#         "question": "What is the result of 10 // 3?",
#         "options": ["3.33", "3", "1", "4"],
#         "answer": "3"
#     },
#     {
#         "question": "Which method converts a string to lowercase?",
#         "options": ["lower()", "casefolding()", "small()", "tolower()"],
#         "answer": "lower()"
#     },
#     {
#         "question": "Which function returns the current working directory?",
#         "options": ["os.listdir()", "os.getcwd()", "os.mkdir()", "os.remove()"],
#         "answer": "os.getcwd()"
#     },
#     {
#         "question": "What does random.shuffle() do?",
#         "options": [
#             "Selects one random item",
#             "Sorts items alphabetically",
#             "Shuffles a mutable sequence in place",
#             "Creates a new list of random numbers"
#         ],
#         "answer": "Shuffles a mutable sequence in place"
#     },
#     {
#         "question": "Which file mode adds content without overwriting existing content?",
#         "options": ["r", "w", "a", "x"],
#         "answer": "a"
#     },
#     {
#         "question": "What does enumerate() return when iterating over a list?",
#         "options": [
#             "Only the values",
#             "Index-value pairs",
#             "Only the indexes",
#             "A sorted list"
#         ],
#         "answer": "Index-value pairs"
#     },
#     {
#         "question": "Which module is designed for generating cryptographically strong random values?",
#         "options": ["random", "secrets", "string", "datetime"],
#         "answer": "secrets"
#     },
#     {
#         "question": "What does os.path.exists(path) check?",
#         "options": [
#             "Whether a path exists",
#             "Whether a file is empty",
#             "Whether a folder is writable",
#             "Whether a path is a Python file"
#         ],
#         "answer": "Whether a path exists"
#     },
#     {
#         "question": "What does time.perf_counter() help measure?",
#         "options": [
#             "Calendar dates",
#             "Elapsed time between events",
#             "Random numbers",
#             "File sizes"
#         ],
#         "answer": "Elapsed time between events"
#     }
# ]

# score = 0
# start_time = time.perf_counter()
# for question in random.sample(questions, 10):
#     print(question["question"])
#     shuffled_options = random.sample(question["options"], len(question["options"]))
#     for i, option in enumerate(shuffled_options, start=1):
#         print(f"{i}. {option}")
#     answer = input("Enter the number of your answer: ").strip()
#     if answer.isdigit() and 1 <= int(answer) <= 4:
#         selected_answer = shuffled_options[int(answer) - 1]
#         print(f"You selected: {selected_answer}")
#         if selected_answer == question["answer"]:
#             print("Correct!")
#             score += 1
#         else:
#             print(f"Incorrect! The correct answer is: {question['answer']}")
#     else:
#         print("Invalid input. Please enter a number between 1 and 4.")

# end_time = time.perf_counter()
# print(f"Your final score is: {score}/10")
# print(f"Time taken: {end_time - start_time:.2f} seconds")

#Q3
import getpass

# otp_file = "otp.txt"

# def generate_otp():
#     otp = str(random.randint(100000, 999999))
#     print(f"OTP sent to your otp.txt file and is valid for 60 seconds.")
#     with open(otp_file, "w", encoding="utf-8") as f:
#         f.write(otp)
#     return otp

# def get_otp():
#     try:
#         with open(otp_file, "r", encoding="utf-8") as f:
#             otp = f.read().strip()
#         return otp
#     except FileNotFoundError:
#         print("OTP file not found.")
#         return None

# def login_history(success):
#     history_file = "login_history.txt"
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     status = "Success" if success else "Failure"
#     with open(history_file, "a", encoding="utf-8") as f:
#         f.write(f"{timestamp} - Login {status}\n")
    
# def main():
#     attempts = 3
#     while attempts > 0:
#         otp = generate_otp()
#         start_time = time.perf_counter()
#         login_success = False
#         duration = 60  # OTP validity duration in seconds
#         elapsed_time = time.perf_counter() - start_time
#         remaining = 60 - elapsed_time
#         if remaining <= 0:
#             print("OTP has expired.")
#             break
#         user_otp = getpass.getpass("Enter the OTP: ")
#         elapsed = time.perf_counter() - start_time
#         if elapsed >= duration:
#             print("OTP has expired.")
#             break
#         if user_otp == otp:
#             print("Login successful!")
#             login_success = True
#             break
#         attempts -= 1
#         print(f"Incorrect OTP. You have {attempts} attempts left.")

#     login_history(login_success)
#     if not login_success:
#         print("Login failed. Please try again later.")  
#     else:
#         print("Welcome to the system!")

# if __name__ == "__main__":
#     main()

#Q4
import shutil

EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".doc", ".docx", ".txt"],
    "Music": [".mp3", ".wav", ".flac"]
}

LOG_FILE = "file_organizer_log.txt"

def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder
    return "Others"

def get_unique_path(folder, filename):
    name, ext = os.path.splitext(filename)
    destination = os.path.join(folder, filename)
    counter = 1
    while os.path.exists(destination):
        new_filename = f"{name}_{counter}{ext}"
        destination = os.path.join(folder, new_filename)
        counter += 1
    return destination

def sort_files(folder_path):
    for file in os.listdir(folder_path):
        if os.path.splitext(file)[1].lower() == ".py":
            continue
        
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            folder = get_destination_folder(file)
            dest_folder_path = os.path.join(folder_path, folder)

            os.makedirs(dest_folder_path, exist_ok=True)

            shutil.move(full_path, get_unique_path(dest_folder_path, file))
            log_entry = f"Moved {file} to {folder}\n"
            with open(LOG_FILE, "a", encoding="utf-8") as log_file:
                log_file.write(log_entry)

            print(f"Moved {file} to {folder}")
if __name__ == "__main__":
    folder_path = input("Enter the folder path or leave blank: ").strip()
    folder = folder_path or os.getcwd()

    if not os.path.isdir(folder):
        print(f"Invalid folder path: {folder}")
    else:
        sort_files(folder)
        print("File sorting completed.")
