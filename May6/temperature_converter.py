def convert_temperature():
    print("Choose the conversion:")
    print("1. Celsius to Fahrenheit")  # Option 1: Celsius to Fahrenheit
    print("2. Fahrenheit to Celsius")  # Option 2: Fahrenheit to Celsius

    # Ask the user to select a conversion option
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        # Ask user for temperature in Celsius and convert to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit}°F")  # Print the converted temperature
    elif choice == "2":
        # Ask user for temperature in Fahrenheit and convert to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius}°C")  # Print the converted temperature
    else:
        print("Invalid choice. Please choose 1 or 2.")  # Error message if invalid choice is entered

# Call the function to start the conversion process
convert_temperature()
