import random

fileName = "Job28.txt"
currentWord = ""
backing = {}

length = 1000

with open(fileName, "r", encoding="utf-8") as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            backing[currentWord] = backing.get(currentWord, {})
            backing[currentWord][word] = backing[currentWord].get(word, 0) + 1
            currentWord = word

def nextWord(input: str):
    if input not in backing:
        return nextWord('')
    
    options = backing.get(input)

    return random.choices(list(options.keys()), list(options.values()), k=1)[0]


lastWord = ''
for i in range(length):
    currentWord = nextWord(lastWord)
    print(currentWord, end=" ")
    lastWord = currentWord



