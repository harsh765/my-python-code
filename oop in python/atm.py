class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount. Deposit amount must be greater than zero."
        self.balance += amount
        return f"${amount} deposited successfully. Current balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount. Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return "Insufficient funds. Unable to process the withdrawal."
        self.balance -= amount
        return f"${amount} withdrawn successfully. Current balance: ${self.balance}"


def main():
    atm = ATM(1000)  # Initial balance

    while True:
        print("ATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            balance = atm.check_balance()
            print(f"Current balance: ${balance}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            result = atm.deposit(amount)
            print(result)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            result = atm.withdraw(amount)
            print(result)
        elif choice == '4':
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
