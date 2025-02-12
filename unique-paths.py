class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        In this efficient solution, we know that the top row and col can be reached only in one possible way
        Use this to build the solution
        """
        row = m
        col = n
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(col):
            dp[0][i] = 1
        for i in range(row):
            dp[i][0] = 1
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[row-1][col-1]