my_name = "John Doe"
print("Hello, my name is " + my_name + ".")
print("This is a string {}".format("INSERT_YOUR_STRING_HERE"))
print("The {} {} {}".format("fox", "brown", "quick"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {0} {0} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
result = 100 / 777
print(result)
print("The result is {r:1.3f}".format(r=result)) # Format to 3 decimal places using {value:width.precision f}
print("The result is {r:10.3f}".format(r=100 / 777)) # Format to 3 decimal places using {value:width(10(in output).precision f}


#f-strings
name = "John"
print(f"Hello, my name is {name}.")

name = "Sam"
age = 25
print(f"{name} is {age} years old.")
