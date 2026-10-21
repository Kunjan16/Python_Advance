#Set is a data structure that stores unique elements. Sets are defined using curly braces {} or the set() function.
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)  # prints {1, 2, 3}
myset.add(2)  # adding a duplicate element, will not be added to the set
print(myset)  # prints {1, 2, 3}

mylist = [1, 2, 3, 4, 5, 1, 2, 3]
myset = set(mylist)  # converts the list to a set, removing duplicates
print(myset)  # prints {1, 2, 3, 4, 5}

second_set = {4, 5, 6, 7}
second_set.add(8)
print(second_set)  # prints {4, 5, 6, 7, 8}
second_set.remove(4)  # removes the element 4 from the set
print(second_set)  # prints {5, 6, 7, 8}
print(len(second_set))  # prints 4, the number of elements in the set

set_union = myset.union(second_set)  # returns a new set that is the union of myset and second_set
print(set_union)  # prints {1, 2, 3, 4, 5, 6, 7, 8}
set_intersection = myset.intersection(second_set)  # returns a new set that is the intersection of myset and second_set
print(set_intersection)  # prints {5}   

print(myset | second_set)  # prints {1, 2, 3, 4, 5, 6, 7, 8}, union of myset and second_set
print(myset & second_set)  # prints {5}, intersection of myset and second_set
print(myset - second_set)  # prints {1, 2, 3}, elements in myset but not in second_set
print(myset ^ second_set)  # prints {1, 2, 3, 4, 6, 7, 8}, elements in either myset or second_set but not both

#print(myset[0])  # this will throw an error because sets are unordered and do not support indexing
