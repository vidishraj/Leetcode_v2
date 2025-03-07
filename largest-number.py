class Comparable:
    # object that can be sorted thanks to magic methods.
    def __init__(self, num):
        self.value = str(num)
    def __lt__(self, other):
        # '82' is before '824' because '82|824' is greater than '824|82'
        return self.value + other.value > other.value + self.value
    def __gt__(self, other):
        return self.value + other.value < other.value + self.value
    def __eq__(self, other):
        return self.value + other.value == other.value + self.value


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numStrings = [Comparable(n) for n in nums]
        numStrings.sort()
        output = ''.join((e.value for e in numStrings))
        return output.lstrip('0') or '0'