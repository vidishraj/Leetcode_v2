import re
from typing import List
import copy
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letterCount = defaultdict(int)
        totalCount = 0
        for letter in licensePlate:
            if letter.isalpha():
                totalCount+=1
                letterCount[letter.lower()]+=1
        # Apply regex substitution
        res = None
        words = sorted(words,key = lambda a: len(a) )
        for word in words:
            tempLetterCount = copy.deepcopy(letterCount)
            matches = 0
            for letter in word:
                if tempLetterCount[letter]>0:
                    tempLetterCount[letter]-=1
                    matches+=1
            if matches == totalCount and (res is None or len(res)>len(word)):
                return word
        return res
