from copy import deepcopy
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Build the solution, for each closest to bottom right, find the 
        cost to get there 
        """
        m = len(grid)
        n = len(grid[0])
        dp =[[0 for i in range(n)] for j in range(m)] 
        # dp init
        dp[m-1][n-1] = grid[m-1][n-1]
        for i in range(n-2, -1, -1):
            dp[m-1][i] += dp[m-1][i+1]+grid[m-1][i]
        for i in range(m-2, -1, -1):
            dp[i][n-1] += dp[i+1][n-1]+grid[i][n-1]
        # print(dp)
        # For every index find min cost of dp bottom and dp[right]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                currGrid = grid[i][j]
                dp[i][j] = min(currGrid+dp[i+1][j], currGrid+dp[i][j+1])
        return dp[0][0]
                


    
            