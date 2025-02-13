class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # We want to store continuous ones above and to the left of a position
        # We will use this to build bigger squares by travelling the diagonal from each spot 

        #0 index for top and 1 index for left
        dpRight = [[0 for i in matrix[0]] for j in matrix]
        dpTop = [[0 for i in matrix[0]] for j in matrix]
        def checkIndex(i,j, level):
            if matrix[i][j]=="0" or dpRight[i][j]<level or dpTop[i][j]<level:
                return level - 1
            return checkIndex(i-1, j-1, level+1)
        m = len(matrix)
        n = len(matrix[0])

        for rowNum in range(0,m):
            onesInRow = 0
            for colNum in range(n-1, -1, -1):
                val = int(matrix[rowNum][colNum])
                dpRight[rowNum][colNum] += onesInRow+val
                if val == 0:
                    onesInRow = 0
                onesInRow+=val
        for i in range(0, n):
            onesInCol = 0
            for j in range(m-1, -1, -1):
                val = int(matrix[j][i])
                dpTop[j][i] += onesInCol + val
                if val == 0:
                    onesInCol = 0
                onesInCol += val

        sol = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j<sol:
                    break
                if matrix[i][j] == "1":
                    sol = max(sol, checkIndex(i, j, 1), 1)
            if i<sol:
                break

        return sol * sol



