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