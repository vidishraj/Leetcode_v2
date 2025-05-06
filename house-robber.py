class Solution:
    dp:list
    def __rob(self, nums, i):
        if i<0:
            return 0 
        if self.dp[i]>=0:
            return self.dp[i]
        self.dp[i] = max(self.__rob(nums, i-1), self.__rob(nums, i-2)+nums[i])
        return self.dp[i]
    def rob(self, nums: List[int]) -> int:
        self.dp = [-1 for i in range(len(nums))]
        self.__rob(nums, len(nums)-1)
        return self.dp[len(nums)-1]