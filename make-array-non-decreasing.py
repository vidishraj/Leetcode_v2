class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        # Use a stack to keep the generated maximum value along the way?
        stack = []
        for num in nums:
            currMax = num
            while stack and stack[-1]>currMax:
                currMax = max(currMax, stack.pop())
            stack.append(currMax)
        return len(stack)