class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Find the sum , find the difference from a multiple from 5, both up and down, 
        Check if we can do that many operations, else return the sum(need to make everything 0)
        """

        sumOfArr = sum(nums)
        if sumOfArr<k:
            return sumOfArr
        return sumOfArr%k