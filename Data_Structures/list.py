letters = ['a', 'b', 'c', 'd', 'e']
matrix = [[0, 'a'], [1, 'b'], [2, 'c'], [3, 'd'], [4, 'e']]
zeros = [0] * 5
print(zeros)  # prints [0, 0, 0, 0, 0]
combined = letters + zeros
print(combined)  # prints ['a', 'b', 'c', 'd', 'e', 0, 0, 0, 0, 0]
number = list(range(5))  # prints [0, 1, 2, 3, 4]
print(number)
chars = list("Hello World")  # prints ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(chars)
print(len(chars))  # prints 11
print(letters[0])  # prints 'a'
print(letters[-1])  # prints 'e'
print(letters)
print(letters[1:4])  # prints ['b', 'c', 'd']
print(letters[::2])  # prints ['a', 'c', 'e']
print(letters[::-1])  # prints ['e', 'd', 'c', 'b', 'a']
print(letters[:])  # prints ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5]
first = numbers[0]
second = numbers[1]
third = numbers[2]
fourth = numbers[3]
fifth = numbers[4]

first, second, third, fourth, fifth = numbers #what we have here is same as above but in a single line
first, second, *others = numbers
print(first)   # prints 1
print(second)  # prints 2   
print(others)  # prints [3, 4, 5]
print(first, second, third, fourth, fifth)  # prints 1 2 3 4 5
first, *middle, last = numbers
print(first)   # prints 1   
print(middle)  # prints [2, 3, 4]  
print(last)    # prints 5
first, *middle, second_last, last = numbers
print(first)        # prints 1  
print(middle)       # prints [2, 3]
print(second_last)  # prints 4
print(last)         # prints 5

for letter in enumerate(letters):
    print(letter)
    print(f"Index: {letter[0]}, Letter: {letter[1]}")

for index, letter in enumerate(letters):
    print(f"Index: {index}, Letter: {letter}")

for letter in enumerate(letters):
    print(letter[0], letter[1])

items = [0, "a"]
index, letter = items
print(index)  # prints 0

item = (0, "a")
index, letter = item
print(index)  # prints 0

for index, letter in enumerate(letters):
    print(index, letter)

#Adding elements to a list
letters.append('f')
print(letters)  # prints ['a', 'b', 'c', 'd', 'e', 'f']
letters.insert(0, 'z')
print(letters)  # prints ['z', 'a', 'b', 'c', 'd', 'e', 'f']
#Removing elements from a list  
letters.remove('c')
print(letters)  # prints ['z', 'a', 'b', 'd', 'e', 'f']
popped = letters.pop()
print(popped)  # prints 'f'
print(letters)  # prints ['z', 'a', 'b', 'd', 'e']
letters.pop(0)  
print(letters)  # prints ['a', 'b', 'd', 'e']
letters.remove('b')
print(letters)  # prints ['a', 'd', 'e']
del letters[1]
print(letters)  # prints ['a', 'e']     
del letters[0:3] # removes elements from index 0 to 2
letters.clear()  # removes all elements from the list
print(letters)  # prints []

#Finding elements in a list
letters = ['a', 'b', 'c', 'd', 'e'] 
print(letters.index('c'))  # prints 2
if 'g' in letters:
    print(letters.index('g'))  # raises ValueError as 'g' is not in the list

letters.count('a')  # prints 1
letters.append('a') 
print(letters.count('a'))  # prints 2

#Sorting a list
my_list = [3, 2, 7, 5, 6, 1]
my_list.sort()  
print(my_list)  # prints [1, 2, 3, 5, 6, 7]

my_list.sort(reverse=True)
print(my_list)  # prints [7, 6, 5, 3, 2, 1]
print(sorted(my_list))  # prints [1, 2, 3, 5, 6, 7]
print(sorted(my_list, reverse=True))  # prints [7, 6, 5, 3, 2, 1]

items = [('item1', 5), ('item2', 3), ('item3', 8)]

def sort_item(item):
    return item[1]
items.sort(key=sort_item)
items.sort(key=lambda item: item[1])#To define a function that we only need to use once, we can use a lambda function instead of defining a separate function.
print(items)  # prints [('item2', 3), ('item1', 5), ('item3', 8)]

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = []
for item in items:#the better way to do this is to use map function which is more efficient than using a for loop
    prices.append(item[1])
print(prices)  # prints [10, 9, 12] 

prices = list(map(lambda item: item[1], items)) #this is the better way to do this using map function
print(prices)  # prints [10, 9, 12]

result = list(map(lambda item: item[1] >=10, items)) #this will return a list of boolean values indicating whether the price is greater than or equal to 10
print(result)  # prints [True, False, True]

filtered = list(filter(lambda item: item[1] >= 10, items)) #this will return a list of items that have a price greater than or equal to 10
print(filtered)  # prints [('Product1', 10), ('Product3', 12)]

