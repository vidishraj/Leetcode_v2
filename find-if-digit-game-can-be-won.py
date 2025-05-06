class Solution:
    
    def checkSingleNumber(self, nums):
        sum1 = 0
        for num in nums:
            if num<10:
                sum1+=num
        return sum1
    def checkWholeSum(self, nums):
        sum2 = 0
        for num in nums:
            sum2+=num
        return sum2
    def checkDoubleNumberSum(self, nums):
        sum3 = 0
        for num in nums:
            if num>9 and num<100:
                sum3+=num
        return sum3
                
    def canAliceWin(self, nums: List[int]) -> bool:
        singleSum = self.checkSingleNumber(nums)
        wholeSum = self.checkWholeSum(nums)
        doubleSum = self.checkDoubleNumberSum(nums)
        if singleSum>(wholeSum-singleSum) or (doubleSum>wholeSum-doubleSum):
            return True
        return False