"""https://codeforces.com/gym/418150/problem/D"""

from collections import Counter


def isStudentExcellent(name):
    char_count = Counter(name)

    min_char_freq = min(char_count.values())
    max_char_freq = max(char_count.values())

    if min_char_freq == max_char_freq:
        return True

    return False


# Prepare input
n_students = int(input())

students = input().split(" ")

bad_students = input().split(" ")

students = set(students)
bad_students = set(bad_students)

unflagged = students - bad_students

# check all unflagged students
excellent_counter = 0
for student in unflagged:
    if isStudentExcellent(student):
        excellent_counter += 1

print(excellent_counter)
