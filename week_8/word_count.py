"""https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

total_words = int(input())
word_count = {}

for i in range(total_words):
    word = input()
    if word_count.get(word):
        word_count[word] += 1
    else:
        word_count[word] = 1

print(len(word_count))
print(" ".join(map(str, word_count.values())))
