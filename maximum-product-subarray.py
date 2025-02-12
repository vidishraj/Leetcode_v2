class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Run product mul from both sides
        """
        frontMul = nums[0]
        frontRes = frontMul
        reverseMul = nums[-1]
        reverseRes = reverseMul 
        for i in range(1,len(nums)):
            if frontMul!=0:
                frontMul *= nums[i]
                if frontRes<frontMul:
                    frontRes = frontMul
            else:
                frontMul = nums[i]
            if reverseMul!=0:
                reverseMul *= nums[-1-i]
                if reverseRes<reverseMul:
                    reverseRes = reverseMul
            else:
                reverseMul =  nums[-1-i]
        return max(reverseRes, frontRes, max(nums))