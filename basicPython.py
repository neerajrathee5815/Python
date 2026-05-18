age = input("Please enter your age : ")

def voting_machine(age) :
    if (int(age) < 18 ):
        print("You are not eligible to vote")
    else:
        print("You can vote")

voting_machine(age)

Task 1
name = "Neeraj"
age = 30
goal_salary = "12LPA"

#Task 2
a = 25
b = 25

sum = a+b
print(sum)
sub = a-b
print(sub)
mul = a*b
print(mul)
div = a/b
print(div)

#Mini Assignment
name = "Neeraj"
city = "Sonipat"
education = "B.E Chemical with MBA"
college = "PU Chandigarh"
experience = 4
goal = "data scientist"

print(f'My name is {name}')
print(f'I am from {city}')
print(f'I have done {education} from {college}')
print(f'I have {experience} years of experience')
print(f'My goal is to become {goal}')


#IF-ELSE
#Task 1
num1 = int(input("Please enter a number"))

if num1 > 0:
    print("num is positive") 
else:
    print("num is negative")

if num1 % 2 == 0:
    print("num is even")
else:
    print("num is odd")

age = int(input("Please enter your age"))
if age >= 21:
    print("eligible for job")
else:
    print("not eligibile for job")

salary = int(input("Please enter your annual salary"))
if salary > 1000000:
    print("High paying job")
else:
    print("Keep improving")

#Loops

#For Loop 
#Task 1
for i in range(1,11):
    print(i)

#Task2
num1 = int(input("Please enter the starting number from which you want squares"))
num2 = int(input("Plezse enter the number till which you want squares"))
for i in range(num1,num2+1):
    print(i*i)

#Task3
num3 = int(input("Please input the number from which you want even numbers"))
num4 = int(input("Please input the number till which you want even numbers"))
for i in range(num3,num4+1):
    if i % 2 == 0:
        print(i)

#Task4
num5 = int(input("Please enter the number whose multiplication table you want"))
for i in range(1,11):
    print(i*num5)

#Mini Assignment

sum = 0
num6 = int(input("Please enter a number"))
for i in range(1,num6+1):
    sum = sum + i 
print(sum)

#Lists
#Task1
index = 1
a = [1,3,4,5,7]
for i in a:
    print(f'{index} element in list is {i}')
    index = index +1

#Task2
total = 0
for i in a :
    total = total + i
print(f'sum of elements in list is {total}')

#Task3
print(f'max element is list is {max(a)}')

#Task4
names = ["Neeraj","Deepak","Mohit","Rohit","Rakesh"]
for name in names:
    if name.startswith("R"):
        print(name)

#Mini Assignment

marks = [70,80,55,90,95]
total = 0
for mark in marks :
    total = total + mark
print(f'Sum of total marks are {total}')

avg_marks = total/len(marks)
print(f'Average marks are {avg_marks}')
max_marks = max(marks)
print(f'Max marks are {max_marks}')
min_marks = min(marks)
print(f'Min marks are {min_marks}')

