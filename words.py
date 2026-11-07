import random
import time

fileName = "story1.txt"
backing = {}

length = 100

prevWord = ""
currentWord = ""
with open(fileName, "r", encoding="utf-8") as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if not prevWord:
                prevWord = word
                continue
            elif not currentWord:
                currentWord = word
                continue


            backing[(prevWord, currentWord)] = backing.get((prevWord, currentWord), {})
            backing[(prevWord, currentWord)][word] = backing[(prevWord, currentWord)].get(word, 0) + 1
            prevWord = currentWord
            currentWord = word

def nextWord(input: str):
    if input not in backing:
        return nextWord(random.choice(list(backing.keys())))
    
    options = backing.get(input)

    return random.choices(list(options.keys()), list(options.values()), k=1)[0]



(prevLastWord, lastWord) = random.choice(list(backing.keys()))
for i in range(length):
    currentWord = nextWord((prevLastWord, lastWord))
    print(currentWord, end=" ", flush=True)
    prevLastWord = lastWord
    lastWord = currentWord
    time.sleep(0.01)
