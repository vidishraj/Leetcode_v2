from heapq import heappop, heappush
from collections import defaultdict
import sys

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Construct adjacency list
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((cost, v))  # (cost, destination)

        # Step 2: Min-Heap -> (cost, node, stops remaining)
        heap = [(0, src, k + 1)]  # (cost, current node, stops remaining)
        min_cost = { (src, k + 1): 0 }  # Track the min cost for each (node, stops remaining)

        while heap:
            curr_cost, node, stops = heappop(heap)
            
            # If we reached the destination, return the current cost
            if node == dst:
                return curr_cost
            
            # If we have stops left, continue exploring
            if stops > 0:
                for cost, neighbor in graph[node]:
                    new_cost = curr_cost + cost
                    if (neighbor, stops - 1) not in min_cost or new_cost < min_cost[(neighbor, stops - 1)]:
                        min_cost[(neighbor, stops - 1)] = new_cost
                        heappush(heap, (new_cost, neighbor, stops - 1))

        return -1  # No valid route found
