def encrypt(message, key):
    res = ""
    for c in message:
        if(c.isalpha()):
            base = ord('a') if c.islower() else ord('A')
            encrypted_char = (ord(c) - base + key) % 26 + base
            res += chr(encrypted_char)
        else:
            res += c
    return res

def decrypt(message, key):
    return encrypt(message, -key)

command = input("Enter the command E or D: ").strip().lower()
if(command == 'e'):
    message = input("Enter your message: ")
    try:
        key = int(input("Enter the key: "))
        encrypted = encrypt(message, key)
        print("Encrypted message:\n", encrypted)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()
elif(command == 'd'):
    message = input("Enter your message: ")
    try:
        key = int(input("Enter the key: "))
        decrypted = decrypt(message, key)
        print("Decrypted message:\n", decrypted)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()
else:
    print("Invalid command. Please enter E or D.")
    exit()