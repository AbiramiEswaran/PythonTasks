'''
Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
Employee Salary Breakdown
a. Write a program that asks the user for:
employee_name (string)
base_salary (float)
hra_percent (integer)
bonus_amount (float)
'''

name:str=str(input("Enter employee name"))
base_salary:float=float(input("Enter employee salary"))
hra_percent:int=int(input("Enter hra percent"))
bonus_amount:float=float(input("Enter bonus amount"))

'''B. Convert inputs to the correct datatype if required.
Calculate:
 HRA = base_salary * (hra_percent / 100)
 Total Salary = base_salary + HRA + bonus_amount
'''

hra=base_salary*(hra_percent/100)
total_salary=base_salary+hra+bonus_amount

'''
C. Print the output like this:
Employee: Arun
Base Salary: 40000.0
HRA @ 20%: 8000.0
Bonus: 5000.0
Total Salary Payable: ₹53000.0

'''


print("Employee:",name)
print("Base Salary:",base_salary)
print("HRA @ "+ str(hra_percent)+"%: ",hra)
print("Bonus: " + str(bonus_amount))
print("Total salary Payable:  ₹",total_salary)

'''
Use Case 2: Student Result Classification
a. Write a program that takes marks as input (initially as a string).
B. Check if the value can be converted to float.
C. Then classify (try using if condition with the help of AI, however we will learn about if condition soon):
Marks >= 90 --> Outstanding
 Marks >= 75 --> Excellent
 Marks >= 50 --> Pass
 Marks < 50 --> Fail
D. If the input is not numeric, print:
 Invalid marks entered — Please provide numeric input.
'''

mark=input("Enter the mark")
print(type(mark))
if mark.isnumeric():
    mark=float(mark)
    if mark>=90:
        print("Outstanding")
    elif(mark>=75):
        print("Excellent")
    elif mark==50:
        print("Pass")
    elif mark<50:
        print("Fail")
else:
    print("Invalid marks entered — Please provide numeric")


'''Use Case 3: Bug Fixing — Datatype Mismatch
The below code is intended to calculate total price, but it has datatype errors. Fix it.
Incorrect code:
item_name = input("Enter product name: ")
 price = input("Enter price per item: ")
 quantity = input("Enter quantity: ")
total_cost = price * quantity
print("You purchased " + quantity + " units of " + item_name)
 print("Total payable: " + total_cost)
Expected output after fixing:
Enter product name: Notepad
 Enter price per item: 35.50
 Enter quantity: 3
You purchased 3 units of Notepad
 Total payable: 106.5 INR'''

#correct code
item_name = input("Enter product name: ")
price = float(input("Enter price per item: "))
quantity =int(input("Enter quantity: "))
total_cost = price * quantity
print(f"You purchased  {quantity} units of " + item_name)
print(f"Total payable: {total_cost} INR")

'''
H. Python Operators Usecases
Use Case 1: Internet Data Usage Calculator
Write a program that asks the user for:
Total monthly data limit (in GB)
Data used so far (in GB)


Calculate using arithmetic operators:
 Remaining data = limit - used
 Usage percentage = (used / limit) * 100
Print:
Remaining data
Usage percentage rounded to 2 decimals


If usage percentage is greater than or equal to 80, print:
 "Warning: High usage, consider upgrading your plan."
'''
datalimit=float(input("Enter Total monthly data limit in GB: "))
dataused=float(input("Enter data used in GB"))
rem_data=datalimit-dataused
used_percent=(dataused/datalimit)*100
print(f"Remaining data {rem_data} GB")
if round(used_percent,2)>=80:
    print ("Warning: High usage, consider upgrading your plan.")
else:
    print ("All is well")


'''Use Case 2: Shopping Discount Calculation
Write a program that takes:
Original price (float)
Discount percent (int)


Using assignment and arithmetic operators, calculate:
 Discount amount = (price * discount_percent) / 100
 Final price = price - discount_amount
Print:
 Original price, discount applied, and final payable amount.'''

original_price = float(input("Enter Original price: "))
disc_percent=int(input("Enter the disounted percent"))
dis_amt=(price * disc_percent) / 100
final_price=price-dis_amt
print(f"Original price: { original_price}")
print(f"Discount applied: {dis_amt}")
print(f"Final Payable amount {final_price}")


'''

Use Case 3 (Bug Fixing): Logical and Comparison Operator Errors
The following code should determine voting eligibility, but it contains operator mistakes. Fix it.
Incorrect code:
age = input("Enter age: ")
 citizen = input("Are you an Indian citizen? (yes/no)")
if age > "18" and citizen = "yes":
 print("Eligible to vote")
 else:
 print("Not eligible")
Expected behavior:
Convert age to integer before comparison.


Only print "Eligible to vote" if age is 18 or above AND citizen input is "yes" (case-insensitive).
'''

#correct code
age = int(input("Enter age: "))
citizen = input("Are you an Indian citizen? (yes/no)")
if age >=18 and citizen.casefold() == "yes":
 print("Eligible to vote")
else:
 print("Not eligible")



'''
I. Conditional Structure
Use Case 1: Banking Eligibility Check
Write a program that asks the user for:
Age
Monthly income
Conditions:
If age < 18: print "Not eligible for a bank account."
If age >= 18 and income < 15000: print "Eligible for basic savings account."
If age >= 18 and income between 15000 and 50000: print "Eligible for savings + salary account."
If age >= 18 and income > 50000: print "Eligible for premium account."
'''

age = int(input("Enter age: "))
income = int(input("Enter income: "))
if age<18:
    print("Not eligible for bank account.")
elif age>=18 and income < 15000:
    print("Eligible for basic savings account.")
elif age>=18 and 15000 <= income <=50000 :
    print("Eligible for savings + salary account.")
elif age>=18 and income > 50000 :
    print("Eligible for premium account.")


'''Use Case 2: Check room availability
-Check room availability
    - If available:
        - If guest is VIP
            → Offer complimentary upgrade
        - Else if member 5+ years
            → Offer discount
        - Else
            → Standard price
    - Else:
        → Show: "No rooms available"

'''

avail_check=input("Available room availability? (yes/no)")
if avail_check.casefold() == "yes":
    usr_type=input("Enter guest type:")
    if usr_type.casefold() == "vip":
        print("Offer complimentary upgrade")
    elif usr_type.casefold() == "member":
        membership_duration=input("Enter member time:")
        if membership_duration == "5":
            print("Offer discount")
        else:
            print("Your membership time should be more than 5 yrs to avail discount")
    else:
        print("Standard price")
else:
    print("NO ROOM AVAILABLE")

'''Use Case 3 (Bug Fixing): Nested Condition Logic Issue
Fix the following code so that it correctly determines whether the entered temperature indicates normal, fever, 
or high fever.
Incorrect code:
temp = input("Enter body temperature in Celsius: ")
if temp < "37":
 print("Normal temperature")
 elif temp > "37" and temp < "39":
 print("Fever")
 else
 print("High fever")
Expected behavior:
Convert temperature to float before comparison.

Conditions should print:
 Normal temperature (less than 37)
 Fever (between 37 and 39)
 High fever (39 and above)
'''
temp = float(input("Enter body temperature in Celsius: "))
if temp < 37:
    print("Normal temperature")
elif 37 <=temp < 39:
     print("Fever")
else:
 print("High fever")

#correct code
temp = float(input("Enter body temperature in Celsius: "))
if temp < 37:
    print("Normal temperature")
elif 37 <= temp < 39:
     print("Fever")
else:
 print("High fever")


'''J. Looping Constructs
Use Case 1: Table Generator
 Write a program that takes a number from the user and prints the multiplication table 
 from 1 to 10 for that number.
Example:
 If user enters 5, output should be:
 5 x 1 = 5
 5 x 2 = 10
 ...
 5 x 10 = 50

'''
num=int(input("Enter a number:"))
for i in range(1,11):
    print(str(num)+ "*" + str(i) + "=" + str(num*i))

'''Use Case 2: Sum of Even and Odd Numbers
 Write a program that asks the user for a positive integer n.
 Using a loop, calculate and print:
Sum of all even numbers from 1 to n


Sum of all odd numbers from 1 to n
'''
even=0
odd=0
num=int(input("Enter a positive integer:"))
for i in range(1,num+1):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print("Sum of all even numbers from 1 to n",even)
print("Sum of all odd numbers from 1 to n",odd)


''''Use Case 3 (Bug Fixing): Infinite Loop Issue
 Fix the code below so that it prints numbers from 1 to 10 and stops correctly.
Incorrect code:
i = 1
 while i <= 10:
 print(i)
Expected behavior:
 The program must increment i and stop when 10 is printed.

'''
#correct code
i = 1
while i <= 10:
    print(i)
    i+=1

'''K. Collection Types
Use Case 1: Product Price Lookup
Create a dictionary with at least 5 products and their prices.
Ask the user to enter a product name.
If found, print the price.
If not found, print: "Product not available." (Hint: use dictionary_var.get(key) function)
'''
prod_dict={"pen":500,"pencil":10,"scale":20,"eraser":5,"chalk":100}
prod=input("Enter the product name")
for key in prod_dict:
    if str(key).lower() == prod.lower():
        print("Product found !!, Price - ",prod_dict[key])
        break
else:
    print("Product not found !")

'''
Use Case 2: City Entry and Duplicate Removal
Ask the user to enter city names repeatedly.
 Stop when the user types "exit".
Requirements:
Store every entered city name in a list (even if it's repeated).
Also store the cities in a set to maintain only unique values.


Finally print:
The complete list of entered cities (with duplicates).
The set of unique cities (duplicates removed).

'''
city_list=[]
uniq_val=set()
while True:
    a=input("Enter City Name , Type exit to quit")
    if(a.lower() != "exit"):
        city_list.append(a)
        uniq_val.add(a)
    else:
        break
print("City List",city_list)
print("Unique list of cities",uniq_val)


'''Use Case 3 (Bug Fixing): List Index Error
 Fix the following code so that it prints all items correctly without an index error:
Incorrect code:
items = ["Pen", "Book", "Mouse", "Keyboard"]
 i = 0
 while i <= len(items):
 print(items[i])
 i = i + 1
Expected behavior:
 The loop should print all the items exactly once and exit without an error.

'''
items = ["Pen", "Book", "Mouse", "Keyboard"]
i = 0
while i < len(items):
 print(items[i])
 i = i + 1
