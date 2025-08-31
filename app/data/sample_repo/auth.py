# Simple authentication module

def login_user(username, password):
    # Hardcoded credentials for demo
    if username == "admin" and password == "password123":
        return {"username": username, "role": "admin"}
    return None
