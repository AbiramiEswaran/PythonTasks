'''
L. Exception Handling
Use Case 1: Division Safe Calculator
 Ask the user for two numbers.
 Perform division and print the result.
 If the user tries to divide by 0, print:
 "Error: Division by zero is not allowed."
 '''
try:
    num1=int(input("enter a number"))
    num2=int(input("enter another number"))
    ans=num1/num2
except ZeroDivisionError:
    print("Dividing by zero is not possible")
else:
   print(f"Ans is {ans}")
finally:
    print("Execution complete")

'''
Use Case 2: Safe Integer Input
Ask the user to enter a number.
Try converting it to an integer.
If conversion fails, print:
"Invalid input. Please enter a numeric value."
'''

try:
    n=int(input("enter a number"))
except ValueError:
    print("Invalid input. Please enter a numeric value")
else:
    print("Converted ,Pls find the type of the given value is",type(n))
finally:
    print("Execution complete")

'''
Use Case 3 (Bug Fixing): Multiple Exception Handling
 Fix the below code so it handles both invalid
  input and division by zero correctly.
Incorrect code:
num1 = int(input("Enter number 1: "))
 num2 = int(input("Enter number 2: "))
 result = num1 / num2
 print("Result:", result)
Expected behavior:
If user enters non-numeric values → print "Invalid input"
If num2 is zero → print "Cannot divide by zero."
Otherwise print the result.

'''
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    result = num1 / num2
except ZeroDivisionError:
     print("Dividing by zero is not possible")
except ValueError:
    print("Invalid input. Please enter a numeric value")
else:
    print(f"Result is {result}")
finally:
    print("Execution complete")

