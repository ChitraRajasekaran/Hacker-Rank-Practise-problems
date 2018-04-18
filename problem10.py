# Basic data types challenges
# problem10 - finding the percentage
#You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
score_name = input()
for key, value in student_marks.items() :
    if key==score_name: print ("{0:.2f}".format(sum(value)/len(value)))
