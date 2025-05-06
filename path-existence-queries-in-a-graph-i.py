class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        # Build using two pointers and Union-Find
        j = 0
        for i in range(n):
            while j < n and nums[j] - nums[i] <= maxDiff:
                if i != j:
                    union(i, j)
                j += 1
        
        res = []
        for source, destination in queries:
            res.append(find(source) == find(destination))
        
        return res
