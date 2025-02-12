class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        firstCityCost = 0
        refund = []
        for pair in costs:
            firstCityCost += pair[0]
            refund.append(pair[1]-pair[0])
        refund.sort()
        midPoint = int(len(costs) / 2)
        for index in range(0, midPoint):
            firstCityCost += refund[index]
        return firstCityCost