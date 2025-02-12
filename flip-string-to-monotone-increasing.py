class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones_count = 0  # Count of 1s encountered
        flips = 0  # Minimum flips required

        for c in s:
            if c == '1':
                ones_count += 1  # Increment count of 1s
            else:
                # Either flip this 0 to 1, or flip all previous 1s to 0
                flips = min(flips + 1, ones_count)

        return flips
