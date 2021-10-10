# Write your code here :-)
while True :
    n = int(input())
    if n>1 and n<101 :
        break
list = []
for i in range (n):
    element = int(input())
    list.append(element)
max = 0
max_num = 0
for i in range(n):
    if list[i] > max :
        max = list[i]
for i in range(n):
    if list[i] == max :
        max_num +=1
print("max_num=",max_num)
if max_num == 1 :
    list.remove(max)
    for i in range (n-1):
        print(list[i], end=' ')
rank = 0
if (max_num > 2):
    for i in range(n):
        if list[i] == max:
            rank += 1
        if rank != 3 :
            print(list[i], end=' ')
        if rank == 3:
            rank = 0
