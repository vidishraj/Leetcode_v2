from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        odd_count = 0   # Count of prefix sums that are odd
        even_count = 1   # Count of prefix sums that are even (including initial 0)
        res = 0
        prefix_sum = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 0:
                # Even prefix sum -> Add all previous odd counts
                res += odd_count
                even_count += 1
            else:
                # Odd prefix sum -> Add all previous even counts
                res += even_count
                odd_count += 1
            
            res %= MOD
        
        return res
