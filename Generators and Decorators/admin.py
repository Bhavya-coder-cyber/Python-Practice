from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role == "admin":
            return func(user_role)
        else:
            print("User is not an admin")
            return None #Not used now but it is a good practice
    return wrapper
@require_admin
def access_to_inventory(role):
    print(f"Accessing inventory for {role}")

access_to_inventory("admin")
access_to_inventory("user")