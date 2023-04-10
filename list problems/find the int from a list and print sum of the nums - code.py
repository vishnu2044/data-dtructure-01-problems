"""
from combination of int and string find the sum of the integer numbers :1
"""

lst = ["d", 1, 2, "a", 3, "f", 4, 5, 9]

sum = 0
for i in lst:
    if type(i) is int:
        sum += i
print("The sum of the integer in the list  :", sum)