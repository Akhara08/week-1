def login():
    # Predefined correct username and password
    correct_username = "admin"
    correct_password = "password123"

    # Ask user to input username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if input matches correct credentials
    if username == correct_username and password == correct_password:
        print("Login successful!")  # Display success message if credentials are correct
    else:
        print("Invalid credentials. Please try again.")  # Display error message if credentials are incorrect

# Call the login function to initiate login process
login()

