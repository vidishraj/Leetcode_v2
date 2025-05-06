class Solution:
    def validPalindrome(self, s: str) -> bool:
        #Iterate from the front and back, remove the first char,
        # Check if it works. if yes, okay,  else no
        start = 0 
        end = len(s)-1
        while start<end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                #Check which char to skip 
                return self.validPalindromeUtil(s, start + 1, end) or self.validPalindromeUtil(s, start, end - 1)
        return True
        
    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True