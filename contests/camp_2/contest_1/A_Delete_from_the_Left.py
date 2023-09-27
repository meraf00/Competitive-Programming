word1 = list(reversed(input()))
word2 = list(reversed(input()))

i = 0 
for char1, char2 in zip(word1, word2):
    if char1 != char2:
        break

    i += 1

print(len(word1) + len(word2) - 2 * i)