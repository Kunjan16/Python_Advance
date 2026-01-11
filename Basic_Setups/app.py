print("Hello World")
print("*" * 10)
student_count = 1000
age = 20
age = "Python"
print(age)
x=1
print(id(x))  # prints the memory address of variable x

x = x + 1
print(id(x))  # prints the memory address of variable x after increment(Since integers are immutable, a new memory address is assigned)

x = [1, 2, 3]
print(id(x))  # prints the memory address of variable x

x.append(4)
print(id(x))  # prints the memory address of variable x after modification (Since lists are mutable, the same memory address is used)

course = "Python Programming"
print(len(course))  # prints the length of the string stored in variable course
print(course[0])  # prints the first character of the string stored in variable course
print(course[-1])  # prints the last character of the string stored in variable course
print(course[0:5])  # prints the substring from index 0 to 5 of the string stored in variable course, characters at index 5 is not included
print(course[:5])  # prints the substring from start to index 5 of the string stored in variable course
print(course[0:])  # prints the substring from index 0 to end of the string stored in variable course
print(course[:])  # prints the entire string stored in variable course

print(id(course))  # prints the memory address of variable course
print(id(course[0]))  # prints the memory address of the first character of the string stored in variable course
# Strings are immutable, so modifying a character will create a new string
course = "Java Programming"
print(id(course))  # prints the memory address of variable course after modification    
print(id(course[0]))  # prints the memory address of the first character of the modified string stored in variable course

message = 'Python "Programming is fun!'
print(message)

msg = "Python \"Programming is fun!"
print(msg)

msgs = "Python \nProgramming is fun!"
print(msgs)

msgss = """Python 
Programming
is fun!"""
print(msgss)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

first_name = "John"
last_name = "Doe"   
full = f"{first_name} {last_name}"
print(full)

full = f"{len(first_name)} {last_name}"
print(full)

full = f"{len(first_name)} {2 + 2}"
print(full)

name = "    Kunjan Singh"
print(name.lower())  # prints the string in lowercase
print(name.upper())  # prints the string in uppercase
print(name.title())  # prints the string in title case
print(name.strip())  # prints the string after removing leading and trailing whitespaces
print(name.find("Sing"))  # prints the starting index of the substring "Singh"
print(name.find("sing"))  # prints -1 as the substring "sing" is not found (case-sensitive)
print(name.replace("K", "-"))  # prints the string after replacing "K" with "-"
print("Kunjan" in name)  # prints True if "Kunjan" is found in the string, else False
print("kunjan" in name)  # prints False as the search is case-sensitive
print("Kunjan" not in name)  # prints False if "Kunjan" is found in the string, else True

course = "Python Programming"
print(course.replace("Python", "Java"))  # prints the string after replacing "Python" with "Java"
print(course.replace("python", "Java"))  # prints the original string as "python" is not found (case-sensitive)

x = 10
x = 0b1010  # binary representation of 10
print(x)  # prints 10
print(bin(x))  # prints the binary representation of x

x = 0x12c  # hexadecimal representation of 300
print(x)  # prints 300
print(hex(x))  # prints the hexadecimal representation of x

x = 10 + 3
x = 10 - 3
x = 10 * 3
x = 10 / 3  # prints 3.3333333333333335
x = 10 // 3  # prints 3
x = 10 % 3  # prints 1
x = 10 ** 3  # prints 1000
print(x)  # prints the value of x

x = x + 3
x += 3
print(x)  # prints the value of x after addition

PI = 3.14 # we use uppercase letters to indicate that this variable is a constant and should not be changed
print(round(PI))  # prints 3
print(abs(-PI))  # prints 3.14

import math
PI = -3.14
print(math.floor(PI))  # prints -4
print(math.ceil(PI))  # prints -3

x = input("Enter a number: ")  # takes input from the user as a string

print(int(x))
print(float(x))
print(bool(x))

print(bool(0))  # prints False
print(bool(""))  # prints False
print(bool(None))  # prints False
print(bool([]))  # prints False
print(bool(25))  # prints True

age = 22
if age >= 18:
    print("You are an adult.")
    print("You can vote.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

print("All Done!")
xyz = 0
if xyz > 1:
    pass #without pass statement, it will give IndentationError, pass is used as a placeholder and does nothing
else:
    pass  # placeholder for future code     

name = " "
if not name.strip():
    print("Name is empty")

if age >= 18 and age < 65:
    print("You are eligible to work.")    #18 <= age < 65
if 18 <= age < 65:
    print("You are eligible to work.")    

age = 25
if age >= 18:
    message = "You are an adult."   
else:
    message = "You are a child."
# Ternary Operator in Python
message = "You are an adult." if age >= 18 else "You are a child."
print(message)   

for x in "Python":
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

for x in range(5):
    print(x)  

for x in range(2, 5):
    print(x)

for x in range(2, 10, 2):
    print(x)

print(type(range(5)))  # prints <class 'range'>

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
found = False
for name in names:
    if name.startswith("J"):
        print("Found!")
        found = True
        break
if not found:
    print("Not Found!")  

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
for name in names:
    if name.startswith("J"):
        print("Found!")
        break
else:# this else corresponds to for loop, it will be executed only if the loop is not terminated by break statement
    print("Not Found!")  

guess = 0
answer = 5
while answer != guess:
    guess = int(input("Enter your guess: ")) 
else:# this else corresponds to while loop, it will be executed only if the loop is not terminated by break statement
    print("You guessed it right!")


def increment(number, by):
    pass  # placeholder for future code     
print(increment(2, 3))

def increment(number: int, by: int) -> tuple:
    return (number, number + by)
print(increment(2, 3))

def multiply(a, b):
    return a * b
multiply(2, 3)

def multiply(list):
    for x in list:
        print(x * 2)
multiply([2, 3, 4, 5])

def multiply(*list):#*list is used to pass variable number of arguments to the function
    total = 1
    for number in list:
        total *= number
    return total
print(multiply(2, 3, 4, 5))     

def save_user(**user):#**user is used to pass variable number of keyword arguments to the function
    print(user)

save_user(id=1, name="John", age=25)
save_user(id=2, name="Jane", age=30, city="New York")   
def save_user(id, name, age=18):#age has a default value of 18
    print(f"ID: {id}, Name: {name}, Age: {age}")
save_user(1, "John")
save_user(2, "Jane", 25)        
def greet(name):
    def get_message():
        return "Hello "
    result = get_message() + name
    return result


