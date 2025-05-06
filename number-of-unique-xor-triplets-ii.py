class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        countDict = {}
        if len(nums)<3:
            return len(nums)

        # Break down the loops?
        initDict = {}
        for i in range(len(nums)):
            for j in range(i, len(nums)):
               initDict[nums[i]^nums[j]] = True
        for i in list(initDict.keys()):
            for j in nums:
                countDict[i^j] = True
        return len(list(countDict.keys()))