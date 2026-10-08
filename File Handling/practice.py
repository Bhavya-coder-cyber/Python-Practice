#Q1
# try:
#     with open("students.txt", "r", encoding="utf-8") as f:
#         # content = f.read()
#         # print(content)
#         for line in f:
#             content = line.strip().split(",")
#             if (int(content[1]) >= 75):
#                 print(f"Name: {content[0]}, Marks: {content[1]}")

# except FileNotFoundError:
#     print("File not found. Please check the file path and try again.")

#Q2
# try:
#     with open("students.txt", "r", encoding="utf-8") as f:
#         sum = 0;
#         count = 0;
#         max = 0;
#         min = 10000;
#         for line in f:
#             try:
#                 content = int(line.strip())
#                 print(content)
#                 sum += content
#                 count += 1
#                 if content > max:
#                     max = content
#                 if content < min:
#                     min = content
#             except ValueError:
#                 print(f"Invalid data: {line.strip()}. Skipping this line.")
#                 continue
#         print(f"Sum: {sum}, Count: {count}, Max: {max}, Min: {min}")
#         print(f"Average: {sum / count}")
# except FileNotFoundError:
#     print("File not found. Please check the file path and try again.")

#Q3
import os
OUTPUT_FILE = "Valid_data.txt"
ERROR_FILE = "Invalid_data.txt"
try:
    with open("students.txt", "r", encoding="utf-8") as f:
        for line in f:
            try:
                content = line.strip().split(",")
                name = content[0]
                age = int(content[1])
                salary = int(content[2])
                with open("Valid_data.txt", "a", encoding="utf-8") as f:
                    f.write(line.strip() + "\n")
            except ValueError:
                with open("Invalid_data.txt", "a", encoding="utf-8") as f:
                    f.write(line.strip() + "\n")
                continue

except FileNotFoundError:
    print("File not found. Please check the file path and try again.")

try:
    with open("Valid_data.txt", "r") as f:
        sum = 0
        count = 0;
        for line in f:
            content = line.strip().split(",")
            name = content[0]
            age = int(content[1])
            salary = int(content[2])
            sum += salary
            count += 1
            print(f"Name: {name}, Age: {age}, Salary: {salary}")
        print(f"Average Salary: {sum/count}")
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")