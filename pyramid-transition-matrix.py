class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Should we create a dp of first two charMapped-> end, try top in o(26)

        letterForPattern = defaultdict(bool)
        resFound = False
        for pattern in allowed:
            letterForPattern[pattern] = True
        @lru_cache(None)
        def findPattern(currBottom, idx, nextBottom, charIdx):
            nonlocal letterForPattern, resFound
            # print(currBottom, idx, nextBottom)
            if resFound:
                return
            if len(currBottom)==1:
                resFound=True
                return
            if idx==len(currBottom)-1:
                findPattern(nextBottom, 0, "", 0)
                return
            baseLetters = currBottom[idx:idx+2]
            for i in range(charIdx, 26):
                currLetter = chr(ord('A')+i)
                # Check pattern exists
                if letterForPattern[baseLetters+currLetter]:
                    # Use the letter
                    findPattern(currBottom,idx+1,nextBottom+currLetter, 0)
                    letterForPattern[baseLetters+currLetter] = False
                    findPattern(currBottom,idx,nextBottom, i+1)
                    letterForPattern[baseLetters+currLetter] = True
                    
            
        findPattern(bottom, 0,"",0)
        return resFound