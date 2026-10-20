# Dictionary in Python
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are mutable, meaning you can change their content without changing their identity.
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(my_dict)# prints {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(my_dict['key1'])  # prints 'value1'
price_lookup = {'apple': 0.40, 'banana': 0.50, 'orange': 0.60}
print(price_lookup['apple'])  # prints 0.40

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
print(d['k1'])  # prints 123
print(d['k2'])  # prints [0, 1, 2]  
print(d['k3'])  # prints {'insideKey': 100}
print(d['k3']['insideKey'])  # prints 100
print(d['k2'][2])  # prints 2

dic = {'key1' : ['a', 'b', 'c']}
mylist = dic['key1']
print(mylist)  # prints ['a', 'b', 'c']
letters = mylist[2]
print(letters)  # prints 'c'
print(letters.upper())  # prints 'C'

new_dict = {'key1': 1, 'key2': 2}
#Adding elements to a dictionary    
new_dict['key3'] = 3
print(new_dict)  # prints {'key1': 1, 'key2': 2, 'key3': 3}

#overwriting an existing key in a dictionary
new_dict['key1'] = 100  
print(new_dict)  # prints {'key1': 100, 'key2': 2, 'key3': 3}

print(new_dict.keys())  # prints dict_keys(['key1', 'key2', 'key3'])
print(new_dict.values())  # prints dict_values([100, 2, 3])
print(new_dict.items())  # prints dict_items([('key1', 100), ('key2', 2), ('key3', 3)])