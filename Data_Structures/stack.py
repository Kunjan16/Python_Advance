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