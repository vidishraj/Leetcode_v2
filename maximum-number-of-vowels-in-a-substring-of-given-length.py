class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        When processing all the substring, we must think of either string manipulation directly or use sliding window
        since length is k we can use sliding window
        """
        vowels= "aeiou"
        
        maxWindowSize = k
        i=0
        j=0
        globalMax = 0
        localMax = 0
        while(j!=maxWindowSize):
            if s[j] in vowels:
                localMax+=1
                
            j+=1
        globalMax = localMax
        while j<len(s):
            if s[i] in vowels:
                localMax-=1
            if s[j] in vowels:
                localMax+=1
            if localMax>globalMax:
                globalMax = localMax
            i+=1
            j+=1
        return globalMax        