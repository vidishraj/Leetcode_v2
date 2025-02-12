class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numOfOperations=0
        currentRemaining=k
        visitedNums={}
        for i in range(len(nums)-1,-1,-1):
            numOfOperations+=1
            if nums[i]<=k and not visitedNums.get(nums[i]):
                currentRemaining-=1
                if currentRemaining==0:
                    return numOfOperations
            visitedNums[nums[i]]=1
            
        return numOfOperations