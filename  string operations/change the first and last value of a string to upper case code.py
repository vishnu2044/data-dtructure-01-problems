str1 = "bdsflb"
var = ""
for i in range(len(str1)):

    if i == 0 or i == len(str1)-1:
        var += str1[i].upper()
    else:
        var += str1[i]
print(var)