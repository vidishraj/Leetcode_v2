class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(i) for i in digits))
        num = num+1
        return [int(i) for i in str(num)]