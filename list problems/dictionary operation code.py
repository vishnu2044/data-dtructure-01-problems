"""
the provided code stub will read in a dictionary containing value/key pairs of name:
[marks] for a list of students. print the average of the marks array for the student
name provided, showing 2 places after the decimal
"""
n = int(input("Enter the number of students : "))
student_marks = dict()
for _ in range(n):
    name, *line = input("enter your name and mark  :").split()
    scores  = list(map(float, line))
    student_marks[name] = scores
query_name = input("Enter the query name : ")
avg_dict = dict()
for key, val in student_marks.items():
    sum = 0
    avg = 0
    for i in val:
        sum += i
    avg = sum/3
    avg_dict[key] = avg
print(avg_dict[query_name])