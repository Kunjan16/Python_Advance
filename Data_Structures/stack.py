# Stack is a data structure that follows the Last In First Out (LIFO) principle. It is used to store a collection of elements, where the last element added is the first one to be removed. In Python, we can use a list to implement a stack.
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)  # prints [1, 2, 3]
last = browsing_session.pop()
print(last)  # prints 3
# print(browsing_session)  # prints [1, 2]
# print("redirect", browsing_session[-1])  # prints redirect 2
if not browsing_session:#this will be skipped because the list is not empty
    browsing_session[-1] #will throw an error because the list is empty and we are trying to access the last element of an empty list. To avoid this, we can check if the list is empty before trying to access the last element.
    print(browsing_session) # prints []

if browsing_session:
    print("redirect", browsing_session[-1])  # prints redirect 2    
else:
    print("no pages in the browsing session")    