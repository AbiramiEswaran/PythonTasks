#A. Python is an indent based programming language
#The following program throws an indentation error. Correct it and make sure it prints properly.

'''teams = ['Data', 'AI', 'DevOps']
for t in teams:
    print('Hello', t, 'Team from Inceptez Technologies')
    print('Keep Learning and Exploring!')'''

'''B. Commented line in Python
usecase1'''
students = 100
trainers = 2
total = students + trainers
print(total)
    # This code calculates sum of students and trainers

#UseCase 2:
#Convert the below block into a “dead code” using comments, then re-activate it later to print

# print("Welcome to Inceptez Python Learning")

#C. Playing with Quotes
'''Use Case 1:
Create three string variables that correctly store and print:'''

s1='This is Inceptez\'s \"Python\" class for Data Engineers & AI Engineers'
s2="This is Inceptez\'s \"Python\" class for Data Engineers & AI Engineers"
s3='''This is Inceptez\'s \"Python\" class for Data Engineers & AI Engineers'''
print(s1)
print(s2)
print(s3)

'''
Use Case 2:
Write a multiline string using triple quotes that prints:'''

multi_line="""
Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey."""
print(multi_line)

'''D. Let's learn all about VARIABLES
Use Case 1:
Declare variables to store the following details:
- Student Name
- Course Name (e.g., “Python Fundamentals”)
- Training Institute Name (Inceptez Technologies)

Then print a formatted message:
Name: Arun is learning the course Python Fundamentals at the institute Inceptez Technologies
'''
stud_name='Abirami'
course_name='Python Fundamentals'
Training_Institute='Inceptez Technologies'
print("Name: " +stud_name+ " is learning the course "+course_name+" at the institute "+Training_Institute)

'''Use Case 2:
Demonstrate dynamic inference, dynamic typing using with fee by applying .18 gst  and 
prove strongly typing character also by operating it with Eighteen percent gst'''
fee=45000
gst=0.18
gst_calc=fee*gst
total_fees=fee+gst_calc;
print(f"TOTAL FEE {total_fees}")
'''
E. Variables Naming Conventions
Use Case 1:
Identify which variable names below are invalid for Inceptez’s student database:

1) 2student = 'Ravi'
2) _student_id = 1001
3) studentName = 'Priya'
4) class name = 'Python'
5) inceptez_batch = 'Morning'

Answer: 2student,class name

Use Case 2:
Declare 3 variables following naming styles for Inceptez projects:

PascalCase: DataEngineeringBatch
camelCase: dataEngineeringBatch
snake_case: data_engineering_batch'''
DataEngineeringBatch="BdWe49" #assigned sametype of styles in values for understanding
dataEngineeringBatch="bDWe49"
data_engineering_batch="bd_we_49"
print("PASCAL CASE: "+DataEngineeringBatch)
print("CAMEL CASE: "+dataEngineeringBatch)
print("SNAKE CASE: "+data_engineering_batch)
