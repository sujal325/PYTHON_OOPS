# Print a welcome message and instructions for the calculator
print("Welcome to this calculator")

print(
    """
    /////TYPE 1 FOR ADDITION/////
    /////TYPE 2 FOR SUBTRACTION/////
    /////TYPE 3 FOR MULTIPLICATION/////
    /////TYPE 4 FOR DIVISION/////
    """
)


# Define a class named Calculator
class Calculator:
    def __init__(self):
        # Initialize private variables for storing results of operations
        self.__addition = 0
        self.__subtraction = 0
        self.__multiplication = 0
        self.__division = 0

        # Start the calculation process
        self.num()

    # Method to prompt user for operation choice
    def num(self):
        key_ = int(input("TYPE YOU WANT TO DO: "))

        # Check user's choice and call corresponding method
        if key_ == 1:
            self.add()
        elif key_ == 2:
            self.subtract()
        elif key_ == 3:
            self.multiply()
        elif key_ == 4:
            self.divide()
        else:
            print("/////THIS IS NOT VALID/////")

    # Method for addition operation
    def add(self):
        x = int(input("TYPE YOUR FIRST INTEGER: "))
        y = int(input("TYPE YOUR SECOND INTEGER: "))
        self.__addition = x + y
        print(f"RESULT OF ADDITION IS: {self.__addition}")

    # Method for subtraction operation
    def subtract(self):
        x = int(input("TYPE YOUR FIRST INTEGER: "))
        y = int(input("TYPE YOUR SECOND INTEGER: "))
        self.__subtraction = x - y
        print(f"RESULT OF SUBTRACTION IS: {self.__subtraction}")

    # Method for multiplication operation
    def multiply(self):
        x = int(input("TYPE YOUR FIRST INTEGER: "))
        y = int(input("TYPE YOUR SECOND INTEGER: "))
        self.__multiplication = x * y
        print(f"RESULT OF MULTIPLICATION IS: {self.__multiplication}")

    # Method for division operation
    def divide(self):
        x = int(input("TYPE YOUR FIRST INTEGER: "))
        y = int(input("TYPE YOUR SECOND INTEGER: "))
        if y != 0:
            self.__division = x / y
            print(f"RESULT OF DIVISION IS: {self.__division}")
        else:
            print("Cannot divide by zero!")


# Create an instance of the Calculator class to start using the calculator
c = Calculator()
