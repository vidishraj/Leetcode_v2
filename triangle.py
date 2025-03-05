class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # At every level, the number of indicies will increase by one 
        # We can move to i or i + 1
        # Build solution up
        if len(triangle) ==1:
            return triangle[0][0]
        dp = [[ 0 for i in item] for item in triangle]
        dp[-1] = triangle[-1]
        # At least 2 levels
        level = len(triangle) - 2
        while level>-1:
            for idx, item in enumerate(triangle[level]):
                dp[level][idx] = min(item+dp[level+1][idx],item + dp[level+1][idx+1])
            level-=1
        return dp[0][0]

