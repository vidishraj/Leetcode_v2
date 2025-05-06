class Solution:
    def isPalindrome(self, x: int) -> bool:
        strI = str(x)
        if strI[0]=="-":
            return False
        strIR = strI[::-1]
        return strIR==strI