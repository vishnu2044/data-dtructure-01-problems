list1 = [12, 56, 32, 10, 67, 8, 91, 23]
for i in range(len(list1)-1):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)

val = int(input("Enter the value : "))
first = 0
last = len(list1)-1

while first <= last:
    mid = (first + last) // 2
    if list1[mid] == val:
        print(f"value found {mid+1} postion")
        break
    if list1[mid] > val:
        last = mid - 1
    elif list1[mid] < val:
        first = mid + 1
else:
    print("value not found")





# val = int(input("enter the value : "))
# first = 0
# last = len(list1) - 1
# while (first <= last):
#     mid = (first + last) // 2
#     if list1[mid] == val:
#         print(f"value found {mid + 1} position")
#         break
#     else:
#         if list1[mid] < val:
#             first = mid + 1
#         elif list1[mid] > val:
#             last = mid - 1
# else:
#     print("Value not found !!")