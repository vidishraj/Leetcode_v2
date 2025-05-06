class Solution:
    def reverseDegree(self, s: str) -> int:
        letters= 'abcdefghijklmnopqrstuvwxyz'
        letterDict = {}
        for i in range(26):
            letterDict[letters[i]] = 26-i
        res = 0
        for index, letter in enumerate(s):
            res += (index+1)*letterDict[letter]
        return res