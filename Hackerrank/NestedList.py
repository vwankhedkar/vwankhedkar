N = int(input())
student = []
for i in range(N):
    grade = [input(), float(input())]
    student.append(grade)
student = sorted(student, key=lambda x: x[1])
second_highest = student[0][1]
for name, grade in student:
    if grade > second_highest:
        second_highest = grade
        break
print('\n'.join([name for name, grade in sorted(student) if grade == second_highest]))

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

OUTPUT:
Berry
Harry
