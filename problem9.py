# Basic data types challenges
#problem 9 - nested lists
#Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

students = []
n = int(input())
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name,score])
second_lowest = sorted(set([b for a, b in students]))[1]
print('\n'.join([a for a,b in sorted(students) if b == second_lowest]))
