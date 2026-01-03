def simple_login():
    
    # Hardcoded credentials(for practices purposes only)
    stored_username = "admin"
    stored_password = "password123"

    # Get user imput
    username = input("enter username here:")
    password = input("enter password here:")

    # Basic credential check
    if username == stored_username and password == stored_password:
        print("Credentials are correct. Login successful")
        return True
    else:
        print("Invalid credentials. Login failed")

    # Security logging (for practices purposes only)
    print(f"[SECURITY LOG] Attempted login for user: {username}")
    return False

    # Run the simple login simulator
if __name__ == "__main__":
    simple_login()

    

