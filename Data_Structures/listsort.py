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



#Bubble sorting
arr_list = [13, 46, 24, 52, 20, 9]

def bubblesort(arr_list):
    num = len(arr_list)
    for i in range(num):
        for j in range(0, num-i-1):
            if arr_list[j] > arr_list[j+1]:
                arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]

    return arr_list

sorted_list = bubblesort(arr_list)
print(sorted_list)

#Selection Sorting

sort_arr = [13, 46, 24, 52, 20, 9]

def selection_sort(sort_arr):
    n = len(sort_arr)
    for i in range(n):
        least = i
        for j in range(i+1, n):
            if sort_arr[j] < sort_arr[least]:
                least = j
        sort_arr[i], sort_arr[least] = sort_arr[least], sort_arr[i]

    return sort_arr

soretd_sel_arr = selection_sort(sort_arr)
print(soretd_sel_arr)                 

#Question
#Given a list of integers, find the second largest element in the list without sorting it.
my_list = [64, 34, 25, 12, 22, 11, 90]
def find_second_largest(my_list):
    first = second = float('-inf')
    for number in my_list:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second

second_largest = find_second_largest(my_list)
print("Second largest element is:", second_largest)

#Improved Version
def find_second_largest(my_list):
    if len(my_list) < 2:
        return None

    first = second = float('-inf')

    for number in my_list:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    return second if second != float('-inf') else None
second_largest = find_second_largest(my_list)
print("Second largest element is:", second_largest)