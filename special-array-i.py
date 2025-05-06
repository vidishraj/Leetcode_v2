class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        even = nums[0] % 2==0
        for i in range(1, len(nums)):
            if nums[i]%2==0 and even or  nums[i]%2!=0 and not even:
                return False
            even = nums[i] %2 == 0
        return True