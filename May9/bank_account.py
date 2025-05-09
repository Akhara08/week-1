class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0.0

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self._balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        except ValueError as e:
            print("Error:", e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdraw amount must be positive.")
            if amount > self._balance:
                raise ValueError("Insufficient balance.")
            self._balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self._balance:.2f}")
        except ValueError as e:
            print("Error:", e)

    def get_balance(self):
        return self._balance


#  user input
def main():
    owner_name = input("Enter account holder name: ")
    account = BankAccount(owner_name)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            print(f"Current balance: ${account.get_balance():.2f}")
        elif choice == "4":
            print("Thank you for using the Bank Account system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
