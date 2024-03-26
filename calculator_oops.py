class Calculator:
    """Initialization of Object"""
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2

    def Add(self):
        """Adds two numbers"""
        return (f"The sum of two numbers is {self.number1 + self.number2}.")

    def Subtract(self):
        """Subtracts smaller number from larger number."""
        if self.number1 >= self.number2:
            return (f"The difference of two numbers is {self.number1 - self.number2}.")  
        else:
            return (f"The difference of two numbers is {self.number2 - self.number1}.")

    def Multiply(self):
        """Multiplies two numbers"""
        return (f"The product of two numbers is {self.number1 * self.number2}.")

    def Divide(self):
        """Divides two numbers, added exception for Zero."""
        if self.number2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return (f"The division of two numbers is{(self.number1)/(self.number2)}.")

class ScientificCalculator(Calculator):
    """Child class inherits from parent class"""
    def __init__(self, number1, number2):
        super().__init__(number1,number2)

    def square(self):
        """Gives the squares of the two numbers"""
        return (f"The square of both the numbers is {self.number1 ** 2},{self.number2 ** 2}.")
       


try:
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    my_calc = ScientificCalculator(num1, num2)
    print(my_calc.Add())
    print(my_calc.Subtract())
    print(my_calc.Multiply())
    print(my_calc.Divide())
    print(my_calc.square())
except ZeroDivisionError as e:
    print("Error:", e)
except ValueError:
    print("Please enter valid numeric input")
