class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        for row in grid:
            row.sort(reverse= True)
        for i,row in enumerate(grid):
            for item in row:
                if limits[i]>0:
                    candidates.append(item)
                    limits[i]-=1
        candidates.sort(reverse=True)
        candidatesF = candidates[:k]
        maxSum = 0
        for item in candidatesF:
            maxSum+=item
        return maxSum