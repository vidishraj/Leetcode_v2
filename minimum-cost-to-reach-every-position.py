class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res = []
        globalMin = float('inf')
        for i in range(len(cost)):
            globalMin = min(globalMin, cost[i])
            res.append(globalMin)
        return res