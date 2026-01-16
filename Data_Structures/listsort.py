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
