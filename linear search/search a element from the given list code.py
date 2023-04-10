lst = [1, 2, 3, 4, 5, 6, 7, 8]
num = int(input("Enter number : "))
for i in range(len(lst)):
    if lst[i] == num:
        print(f"the {num} value present in the {i+1} position.")
        break
else:
    print(f"the {num} value not present in the list.")

