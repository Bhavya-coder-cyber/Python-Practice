# file = open("sample.txt", "w")
# try:
#     file.write("Hello World")
# finally:
#     file.close()

with open("sample.txt", "w") as file:
    file.write("Hello World1")
with open("sample.txt", "w") as file:
    file.write("Hello World \n")