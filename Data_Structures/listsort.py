my_list = [3,2,7,5,6,1]

n = len(my_list)
for i in range(n):
    for j in range(i+1, n):
        if my_list[i] > my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp
print(my_list)        


for i in range(n):
    least = i
    for j in range(i+1,n):
        if my_list[j] < my_list[least]:
            least = j
    my_list[i], my_list[least] = my_list[least], my_list[i]


#largest element in list
arr = [2,3,5,1,0]
n = len(arr)
largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

print(largest)            


number = [1,2,4,7,7,5]
numbers = sorted(number)

n = len(numbers)
def find_second_element(numbers):
    n = len(numbers)
    first = numbers[0]
    for i in range(n):
        if numbers[i] != first:
            smallest = numbers[i]
            break

    last = numbers[-1]
    for i in range(n-1, -1, -1):
        if numbers[i] != last:
            largest = numbers[i]
            break

    return smallest, largest

second_smallest, second_largest = find_second_element(numbers)
print("Second smallest:", second_smallest)        
print("Second largest:", second_largest)