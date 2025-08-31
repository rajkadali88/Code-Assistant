from auth import login_user
from utils import process_data

def main():
    user = login_user("admin", "password123")
    if user:
        data = ["apple", "banana", "cherry"]
        result = process_data(data)
        print("Processed:", result)
    else:
        print("Login failed.")

if __name__ == "__main__":
    main()
