import random  # Importing the random module to generate a random number

def guessing_game():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0  # Counter to track the number of attempts

    print("Guess a number between 1 and 100")

    while True:
        # Take user's guess as input and convert it to an integer
        guess = int(input("Your guess: "))
        attempts += 1  # Increment the attempt counter

        # Provide feedback to the user based on the guess
        if guess < number:
            print("Too low!")  # If guess is lower than the number
        elif guess > number:
            print("Too high!")  # If guess is higher than the number
        else:
            # If guess is correct, print success message and break the loop
            print(f"Congratulations! You guessed it in {attempts} tries.")
            break

# Call the function to start the game
guessing_game()

