class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        """
        Same concept as min path sum. build solution from bottom
        """
        m = len(grid)
        n = len(grid[0])
        if grid[m-1][n-1]==1:
            return 0
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[m-1][n-1] = 1
        for i in range(n-2,-1,-1):
            if grid[m-1][i]==1:
                dp[m-1][i] = 0
            else:
                dp[m-1][i] = dp[m-1][i+1]
        for i in range(m-2,-1,-1):
            if grid[i][n-1]==1:
                dp[i][n-1] = 0
            else:
                dp[i][n-1] = dp[i+1][n-1]
        for i in range(m-2,-1, -1):
            for j in range(n-2, -1, -1):
                if grid[i][j]!=1:
                    dp[i][j] = dp[i+1][j]+dp[i][j+1]
                else:
                    dp[i][j] = 0
        return dp[0][0]