class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordList = s.split();
        return len(wordList[-1])