import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build Graph as Adjacency List
        graph = {i: [] for i in range(n)}
        for u, v, cost in roads:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        # Step 2: Initialize Dijkstra's Algorithm
        heap = [(0, 0)]  # (cost, node)
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        while heap:
            curr_cost, node = heapq.heappop(heap)
            
            # If we already found a shorter path, ignore this one
            if curr_cost > dist[node]:
                continue
            
            for neighbor, edge_cost in graph[node]:
                new_cost = curr_cost + edge_cost
                
                if new_cost < dist[neighbor]:  # Found a shorter path
                    dist[neighbor] = new_cost
                    ways[neighbor] = ways[node]  # Reset ways count
                    heapq.heappush(heap, (new_cost, neighbor))
                
                elif new_cost == dist[neighbor]:  # Another shortest path
                    ways[neighbor] += ways[node]
        
        return ways[n - 1]%(10**9+7)  # Number of ways to reach the last node
