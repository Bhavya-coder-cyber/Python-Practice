import random
import getpass
import string

def check_password(password):
    issues=[]
    if(len(password) < 8):
        issues.append("Password must be at least 8 characters long")
    if not any(c.islower() for c in password):
        issues.append("Password must contain at least one lowercase letter")
    if not any(c.isupper() for c in password):
        issues.append("Password must contain at least one uppercase letter")
    if not any(c.isdigit() for c in password):
        issues.append("Password must contain at least one number")
    if not any(c in string.punctuation for c in password):
        issues.append("Password must contain at least one special character")
    return issues

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

password = getpass.getpass("Enter your password: ")
issues = check_password(password)

if not issues:
    print("Password is strong")
else:
    print("Password is weak:")
    for issue in issues:
        print(f"- {issue}")
    print("Suggested a good password")
    print(generate_password())