# def sum(n):
#    if n==1:
#        return 1
#    else:
#        return n+sum(n-1)
# print(sum(10))

list1 = [1, 45, 2, 6, 34, 78]
for i in range(len(list1)-1):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)