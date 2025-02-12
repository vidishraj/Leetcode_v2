class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Have to do a running product from both sides and remember it
        """
        dpR = []
        dpL = [1 for num in nums]
        runningMul = 1
        for i in range(len(nums)):
            dpR.append(runningMul)
            runningMul*= nums[i]
        runningMul = 1
        for i in range(len(nums)-1, -1, -1):
            dpL[i] = runningMul
            runningMul *= nums[i]
        res = [1 for num in nums]
        for i in range(len(nums)):
            res[i] = dpL[i]*dpR[i]
        return res