import heapq
from typing import List

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sellHeap = []  # Min heap (default in heapq)
        buyHeap = []   # Max heap (invert prices)

        for price, amount, orderType in orders:
            if orderType == 0:  # Buy order
                while amount > 0 and sellHeap and sellHeap[0][0] <= price:
                    if sellHeap[0][1] <= amount:
                        amount -= sellHeap[0][1]
                        heapq.heappop(sellHeap)
                    else:
                        sellHeap[0][1] -= amount
                        amount = 0
                if amount > 0:
                    heapq.heappush(buyHeap, [-price, amount])

            else:  # Sell order
                while amount > 0 and buyHeap and -buyHeap[0][0] >= price:
                    if buyHeap[0][1] <= amount:
                        amount -= buyHeap[0][1]
                        heapq.heappop(buyHeap)
                    else:
                        buyHeap[0][1] -= amount
                        amount = 0
                if amount > 0:
                    heapq.heappush(sellHeap, [price, amount])

        totalLeft = sum(amount for _, amount in sellHeap) + sum(amount for _, amount in buyHeap)
        return totalLeft % (10**9 + 7)
