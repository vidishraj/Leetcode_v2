class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        # Iterate once and make another array with sum of digits O(n*m)-> Maybe can do this after sorting as well 
        # Sort this and return the last two O(nlogn)
        # Total TC max(O(n•logn), O(n*m))

        sumCheck = defaultdict(lambda:-1)
        nums.sort()
        def sumOfDigits(num):
            numStr = str(num)
            res = 0
            for digit in numStr:
                res+=int(digit)
            return res
        res = -1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            sum = sumOfDigits(num)
            if res-num>nums[-1]:
                # We reach a point where the needed number is larger than highest number
                break
            if sumCheck[sum]!=-1:
                res =max(res, num+sumCheck[sum])
            sumCheck[sum] = num
        return res
