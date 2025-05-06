class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        numCount = Counter()
        # Count the occurence of each letter
        for letter in tiles:
            numCount[letter]+=1
        # To mark unique strings made
        dp=defaultdict(bool)
        total = 0
        @lru_cache(None)
        def backtrack(stringMade):
            nonlocal dp, numCount, tiles, total
            if dp[stringMade]:
                return
            total+=1
            # Mark string visited
            dp[stringMade] = True
            for key in numCount:
                if numCount[key]>0:
                    # Use the letter and remove from counter
                    stringMade+=key
                    numCount[key]-=1
                    backtrack(stringMade[:])
                    # Dont use the letter and add it back to the counter
                    stringMade = stringMade[:-1]
                    numCount[key]+=1
                    backtrack(stringMade[:])
            
        backtrack("")
        
        return total-1 # Accounts for empty string