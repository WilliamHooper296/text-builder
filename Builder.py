import random
import time

class Builder:


    """
    Builds a markov-chain backing dict which is compatable with this Class's read function

    Args:
        inputPath: string path of file to read text from
        order: order of markov-chain dict to build
    """
    def build(self, inputPath: str, order: int):

        backing = {}
        wordsRead = 0
        lastWords = []

        with open(inputPath, "r", encoding="utf-8") as file:

            for line in file:

                words = line.strip().split()

                for word in words:
                    if wordsRead < order:
                        lastWords.append(word)
                        wordsRead += 1
                        continue
                    
                    key = tuple(lastWords)

                    backing[key] = backing.get(key, {})
                    backing[key][word] = backing[key].get(word, 0) + 1 

                    lastWords.pop(0)
                    lastWords.append(word)

        return backing


    def buildMulti(self, inputs: list[str], order: int):
        backing = {}
        for name in inputs:

            wordsRead = 0
            lastWords = []

            with open(name, "r", encoding="utf-8") as file:

                for line in file:

                    words = line.strip().split()

                    for word in words:
                        if wordsRead < order:
                            lastWords.append(word)
                            wordsRead += 1
                            continue
                        
                        key = tuple(lastWords)

                        backing[key] = backing.get(key, {})
                        backing[key][word] = backing[key].get(word, 0) + 1 

                        lastWords.pop(0)
                        lastWords.append(word)

        return backing

    """
    Assembles a paragraph of text from the input markov-chain

    Args:
        backing: markov-chain dict of type {tuple: {string: int}}
        words: int representing the number of words to generate

    Return: None
    """
    def read(self, backing: dict, words: int):

        key = list(random.choice(list(backing.keys())))

        for i in range(words):
            choice = self._nextWord(tuple(key), backing)
            print(choice, end=" ", flush=True)
            key.pop(0)
            key.append(choice)
            time.sleep(0.01)



    def _nextWord(self, input: tuple, backing: dict):
        if input not in backing:
            input = random.choice(list(backing.keys()))
        
        options = backing.get(input)

        return random.choices(list(options.keys()), list(options.values()), k=1)[0]
