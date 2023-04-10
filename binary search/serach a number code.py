
list1 = [1, 4, 56, 90, 123, 145, 456, 678, 900]
val = int(input("enter the value : "))
first = 0
last = len(list1) - 1
while (first <= last):
    mid = (first + last) // 2
    if list1[mid] == val:
        print(f"value found {mid + 1} position")
        break
    else:
        if list1[mid] < val:
            first = mid + 1
        elif list1[mid] > val:
            last = mid - 1
else:
    print("Value not found !!")

