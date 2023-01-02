t = int(input())

for i in range(t):
    line = input().split()

    organized = [""] * (2*10**4 + 1)
    for word in line:
        index = []
        cleaned_word = []
        for char in word:
            if char.isdigit():
                index.append(char)
            else:
                cleaned_word.append(char)

        index = int("".join(index)) - 1
        cleaned_word = "".join(cleaned_word)

        organized[index] = cleaned_word

    print(" ".join(organized).strip())
