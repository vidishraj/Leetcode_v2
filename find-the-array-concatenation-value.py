class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        concatValue=0
        while len(nums)>0:
            if(len(nums)>1):
                concat = nums[0].__str__()+nums[-1].__str__()
                concat= int(concat)
                concatValue+= concat
                nums.pop(0)
                nums.pop(-1)
            else:
                concatValue+=int(nums[0])
                nums.pop(0)
        return concatValue