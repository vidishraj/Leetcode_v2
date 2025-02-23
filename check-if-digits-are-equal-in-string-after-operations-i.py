class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Every iteration we reduce 1 char
        def calculateNewString(oldStr):
            sCpy = ""
            for i in range(0, len(oldStr)-1):
                sCpy+=str((int(oldStr[i])+int(oldStr[i+1]))%10)
            return sCpy
                
        while len(s)>2:
            s = calculateNewString(s)
        return s[0]==s[1]