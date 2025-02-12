class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsCount={}
        for num in nums:
            if numsCount.get(num) is None:
                numsCount[num]=1
            else:
                numsCount[num] += 1
        numOfOperations=0
        for value in numsCount.values():
            if value%3==0:
                numOfOperations+=value/3
            elif value==1:
                return -1
            elif value==2 or value==3:
                numOfOperations+=1
            elif value%3==1:
                numOfOperations+=value/3+1
            elif value%3==2:
                numOfOperations+=value/3+1
        return numOfOperations