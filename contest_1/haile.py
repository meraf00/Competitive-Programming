"""https://codeforces.com/gym/418150/problem/C"""

line = input()

n_students = int(line)

rows = []
for _ in range(n_students):
    line = input()
    student_data = line.replace("#", " ")
    rows.append(student_data)

for row in rows:
    print(row)
