class Solution:
    def maxProduct(self, n: int) -> int:
        numInStr = str(n)
        numList = []
        for digit in numInStr:
            numList.append(digit)
        numList.sort()
        return int(numList[-1])*int(numList[-2])