class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Precompute min/max for each column and row
        topBottom = [[float('inf'), float('-inf')] for _ in range(n+1)]
        leftRight = [[float('inf'), float('-inf')] for _ in range(n+1)]

        for x, y in buildings:
            topBottom[x][0] = min(topBottom[x][0], y)
            topBottom[x][1] = max(topBottom[x][1], y)
            leftRight[y][0] = min(leftRight[y][0], x)
            leftRight[y][1] = max(leftRight[y][1], x)

        res = 0

        for x, y in buildings:
            minRow, maxRow = topBottom[x]
            minCol, maxCol = leftRight[y]
            if minRow < y < maxRow and minCol < x < maxCol:
                res += 1
        
        return res
