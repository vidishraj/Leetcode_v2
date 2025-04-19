class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Sort nums and then find the pair maybe where the sum does not exceed upper 
        # but the sum also where it just exceeds lower? 
        # Adjacent would form the smallest pair and the farthest would be highest pair 
        # Can do it in n2-> nlogn to sort 

        #[0, 1, 4, 4, 5, 7]
        def count(t):
            i, j = 0, len(nums) - 1
            res = 0

            while i < j:
                if nums[i] + nums[j] > t:
                    j -= 1
                else:
                    res += j - i
                    i += 1

            return res

        nums.sort()

        return count(upper) - count(lower - 1)