from collections import defaultdict
from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
            
        q = deque([0])
        visited = {0}
        res = 0
        while q:
            city = q.popleft()
            
            for neighbor, cost in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    res += cost
                    q.append(neighbor)
                    
        return res