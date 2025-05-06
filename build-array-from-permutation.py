class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for index, item in enumerate(nums):
            res.append(nums[nums[index]])
        return res