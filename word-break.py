class Solution:
    wordDict:list
    s:str

    @lru_cache(None)
    def rec(self, start, end):
        if start == len(self.s):
            return True
        if end>len(self.s):
            return False
        if self.s[start:end] in self.wordDict:
            # Can segment here
            return self.rec(end, end+1) or self.rec(start, end+1)
            # Dont segment as well
        else:
            return self.rec(start, end+1)
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Break and start a new chain everytime we find a match
        Once we reach the end of the stirng we are done
        """
        self.wordDict = wordDict
        self.s = s
        return self.rec(0,1)