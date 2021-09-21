totGrades = []
for _ in range(5):
    grades = input()
    grades = grades.split(' ')
    for i in grades:
        i = int(i)
    totGrades.append(grades)
highestGrade = 0
index = 0
for i in range(5):
    pupil = totGrades[i]
    grade = int(pupil[0]) + int(pupil[1]) + int(pupil[2]) + int(pupil[3])
    if grade > highestGrade:
        index = i
        highestGrade = grade
print(f'{index+1} {highestGrade}')