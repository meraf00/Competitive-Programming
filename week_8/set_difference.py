"""https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n_english_students = int(input())
    english_students = input().split()

    n_french_students = int(input())
    french_students = input().split()

    english_students = set(english_students)
    french_students = set(french_students)

    english_only = english_students.difference(french_students)

    print(len(english_only))
