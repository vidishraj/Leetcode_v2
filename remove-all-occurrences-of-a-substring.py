class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        partlen=len(part)
        def findSubStr():
            nonlocal s, part
            try:
                return s.index(part)
            except:
                return -1    
        startIdx = findSubStr()
        while startIdx!=-1:
            s = s[:startIdx]+s[startIdx+partlen:]
            startIdx = findSubStr()
        return s