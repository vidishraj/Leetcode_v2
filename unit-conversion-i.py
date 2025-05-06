from collections import defaultdict, deque
from typing import List

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        ## Maybe move everything to a single BFS?
        aList = defaultdict(list)
        for source, destination, weight in conversions:
            aList[source].append((destination, weight))
            aList[destination].append((source, weight))
        
        MOD = 10**9 + 7
        
        costs = defaultdict(lambda: -1)
        
        q = deque()
        q.append((0, 1))
        costs[0] = 1
        
        while q:
            currNode, currCost = q.popleft()
            for dest, weight in aList[currNode]:
                if costs[dest] == -1:
                    newCost = (currCost * weight) % MOD
                    costs[dest] = newCost
                    q.append((dest, newCost))
        
        res = []
        for i in range(len(conversions)+1):
            res.append(costs[i] if costs[i] != -1 else -1)
        
        return res
