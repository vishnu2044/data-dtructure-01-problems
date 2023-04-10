list1 = ["vishnu", "nandakumar", "pranav", "gokul", "junaid", "josena", "faiz"]
dict = {}
for name in list1:
    dict[name] = 0
    for i in name:
        dict[name] += 1
print(dict)
large = dict["vishnu"]
key_temp =""
for key, value in dict.items():
    if large < value:
        large = value
        key_temp = key

print(large)
print(key_temp)