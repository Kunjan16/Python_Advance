# Tuple is a data structure that is similar to a list, but it is immutable, meaning its elements cannot be changed after creation. Tuples are defined using parentheses ().
point = (1, 2)
print(point)  # prints (1, 2)
points = point + (3, 4)
print(points) # prints (1, 2, 3, 4)
pointss = points * 2
print(pointss) # prints (1, 2, 3, 4, 1, 2, 3, 4)
print(point[0])  # prints 1
print(point[1])  # prints 2
print(point[0:2])  # prints (1, 2)
w, x, y, z = points #this is called unpacking a tuple, we are assigning the values of the tuple to the variables x, y and z
print(w)  # prints 1
print(x)  # prints 2
print(y)  # prints 3
print(z)  # prints 4

if 10 in points:
    print("10 is in the points tuple")  # this will not be printed because 10 is not in the points tuple

# point[0] = 10 #this will throw an error because tuples are immutable and we cannot change the value of an element in a tuple

#we can also convert a list and a string into a tuple using the tuple() function
numbers = [1, 2, 3] 
number_tuple = tuple(numbers)   
print(number_tuple)  # prints (1, 2, 3)
words = "Hello World"
word_tuple = tuple(words)   
print(word_tuple)  # prints ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')