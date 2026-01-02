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