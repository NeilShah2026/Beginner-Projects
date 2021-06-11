# Make A Class
class operators:

    # Add Function
    def add(self, x, y):
        return x + y

    # Subtraction Function
    def subtract(self, x, y):
        return x - y

    # Multiplication Function
    def multiply(self, x, y):
        return x * y

    # Divide Function
    def divide(self, x, y):
        return x // y

# Initilize Our Object (Class)
operators = operators()

# Use Our Functions
sum = operators.add(8, 9)

subtraction = operators.subtract(9, 1)

product = operators.multiply(5, 4)

quotient = operators.divide(10, 5)
