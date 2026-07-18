s = input()
words = s.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word in count:
    print(word.capitalize(), count[word], " ")
