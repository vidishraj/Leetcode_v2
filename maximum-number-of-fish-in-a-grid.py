from collections import deque
class Solution:
    visited:list
    def bfs(self, grid, i , j):
        visited = self.visited
        q = deque()
        def checkIndex(i, j):
            return 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]>0 and visited[i][j]==-1
        q.append((i, j))
        visited[i][j]=1
        tsum = 0 
        while len(q)>0:
            i , j = q.popleft()
            val = grid[i][j]
            tsum+=val
            if checkIndex(i-1, j):
                visited[i-1][j] = 1
                q.append((i-1, j))
            if checkIndex(i+1, j):
                visited[i+1][j] = 1
                q.append((i+1, j))
            if checkIndex(i, j-1):
                visited[i][j-1] = 1
                q.append((i, j-1))
            if checkIndex(i, j+1):
                visited[i][j+1] = 1
                q.append((i, j+1))
        # Do bfs
        return tsum

    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.visited = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
        #Lets do good old bfs traversing from each non-visited point
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]>0) and self.visited[i][j]==-1:
                    c =self.bfs(grid, i, j)
                    res = max(res, c)
        return res