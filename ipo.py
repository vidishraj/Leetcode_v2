import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Min-heap to store projects sorted by required capital
        min_capital_heap = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(min_capital_heap)

        # Max-heap to store affordable projects by profit
        max_profit_heap = []

        p = 0
        while p < k:
            # First while: Move all projects we can afford into the max-profit heap
            while min_capital_heap and min_capital_heap[0][0] <= w:
                cap, prof = heapq.heappop(min_capital_heap)
                heapq.heappush(max_profit_heap, -prof)

            # Second while: Pick the most profitable project (if any)
            if not max_profit_heap:
                break  # No project can be afforded

            w += -heapq.heappop(max_profit_heap)
            p += 1

        return w
