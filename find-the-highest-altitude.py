class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        runningSum = 0 
        res = 0
        for alt in gain:
            runningSum+=alt
            if res<runningSum:
                res = runningSum
        return res
                