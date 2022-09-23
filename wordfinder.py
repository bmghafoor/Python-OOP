"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    def __init__(self,filepath):
        file_contents = open(filepath)

        self.words = self.seperate(file_contents)

        print(f"{len(self.words)} words")

    def seperate(self, arr):
        return [word[0:len(word)-2] for word in arr]

    def random_word(self):
        return random.choice(self.words)


class SpecialWord(WordFinder):
    def seperate(self, arr):
        return [word[0:len(word)-2] for word in arr
        if word[0] != '#']


    



    



