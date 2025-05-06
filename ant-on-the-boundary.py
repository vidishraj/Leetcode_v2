class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        boundary = 0 
        start= 0
        for num in nums:
            start+=num
            if start==0:
                boundary+=1
                
        return boundary