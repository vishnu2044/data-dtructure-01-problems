lst1 = [12, 34, 54, 60, 91, 2, 4, 36]
lst2 = list()
for i in lst1:
    if i % 3 ==0:
        lst2.append(i)
print(lst2)