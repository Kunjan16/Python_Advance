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