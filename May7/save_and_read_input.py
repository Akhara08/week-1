def save_and_read_file(filename):
    try:
        user_input = input("Enter some text to save to the file: ")
        with open(filename, 'w') as file:
            file.write(user_input)
        print("\nData saved successfully!\n")

        with open(filename, 'r') as file:
            content = file.read()
            print("Content read from file:\n", content)

    except IOError:
        print("Error: File could not be written or read.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Example usage
filename = "user_input.txt"
save_and_read_file(filename)
