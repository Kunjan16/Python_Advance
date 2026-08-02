#Queue is a data structure that follows the First In First Out (FIFO) principle. It is used to store a collection of elements, where the first element added is the first one to be removed. In Python, we can use a list to implement a queue.
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2) 
queue.append(3)
print(queue)  # prints deque([1, 2, 3])
queue.popleft()  # removes the first element (1) from the queue
print(queue)  # prints deque([2, 3])

if not queue: #this will be skipped because the queue is not empty
    print("Empty queue") #this will not be printed because the queue is not empty