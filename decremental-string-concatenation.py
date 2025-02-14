from typing import List

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        from functools import lru_cache
        
        n = len(words)
        
        # Memoization using LRU Cache
        @lru_cache(None)
        def dp(index, first, last):
            """Finds the minimum length of the concatenated string."""
            if index == n:  # Base case: all words used
                return 0
            
            currWord = words[index]
            newLen = len(currWord)
            
            # Option 1: Append words[index] at the end
            option1 = (newLen - (last == currWord[0])) + dp(index + 1, first, currWord[-1])
            
            # Option 2: Append words[index] at the beginning
            option2 = (newLen - (currWord[-1] == first)) + dp(index + 1, currWord[0], last)
            
            return min(option1, option2)
        
        # Start recursion with the first word’s first and last character
        return len(words[0]) + dp(1, words[0][0], words[0][-1])
