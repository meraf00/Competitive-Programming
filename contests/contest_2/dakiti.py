word_count = int(input())

for i in range(word_count):
    line = input().split()

    organized = [""] * (2*10**4+1)

    for word in line:
        cleaned_word = []
        i = 0
        index = ""
        while i < len(word):
            char = word[i]
            if char.isdigit():
                while i < len(word) and word[i].isdigit():
                    index += word[i]
                    i += 1
            else:
                cleaned_word.append(char)
                i += 1

        index = int(index) - 1
        organized[index] = "".join(cleaned_word)

    print(" ".join(organized).strip())
