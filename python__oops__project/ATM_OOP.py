class ATM:
    def __init__(self):
        print("Welcome to ATM")
        print(
            """
            Type 1 for Balance deposit 
            Type 2 for Balance credit
            Type 3 for Check Balance
            """
        )

        self.key = ""
        self.balance = 1000  # Initial balance set to 1000
        self.atm()

    def atm(self):
        key = input("Enter your key: ")

        if key == "1":
            self.deposit()

        elif key == "2":
            self.credit()

        elif key == "3":
            self.check_balance()

        else:
            print("Invalid input. Please enter 1, 2, or 3.")
            self.atm()  # Restart ATM operation

    def deposit(self):
        deposit_amount = int(input("Enter the amount you want to deposit: "))
        self.balance += deposit_amount
        print(
            f"Your deposit of {deposit_amount} was successful. Your new balance is {self.balance}"
        )

    def credit(self):
        credit_amount = int(input("Enter the amount you want to withdraw: "))
        if credit_amount > self.balance:
            print(
                f"You do not have sufficient funds. Your current balance is {self.balance}"
            )
        else:
            self.balance -= credit_amount
            print(
                f"{credit_amount} has been withdrawn from your account. Your new balance is {self.balance}"
            )

    def check_balance(self):
        print(f"Your current balance is {self.balance}")


# Create an instance of the ATM class to start using the ATM simulation
s = ATM()
