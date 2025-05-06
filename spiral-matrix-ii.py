class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 0 - > Right, 1 -> Down, 2-> Left, 3-> Up
        # Dictionary will tell up when to turn
        changeDirection = {
            0: 1,
            1: 2,
            2: 3,
            3: 0
        }
        squared = n * n
        start = 1 
        stepsToGo = n - 1
        direction = 0
        
        rowIndex = 0
        colIndex = 0 
        res = [[0 for i in range(n)] for i in range(n)]
        dp = defaultdict(lambda:False)
        while start != squared:
            res[rowIndex][colIndex] = start
            dp[start] = True
            if direction == 0:
            # Travelling right
                if colIndex+1 == n or dp[res[rowIndex][colIndex+1]]:
                    direction = 1
                    # Have to change direction
                else:
                    colIndex+=1
                    start+=1
            elif direction == 1:
            # Travelling Down 
                if rowIndex+1 == n or dp[res[rowIndex+1][colIndex]]:
                    direction = 2
                    # Have to change direction
                else:
                    rowIndex+=1
                    start+=1
            elif direction == 2:
                #Travelling Left
                if colIndex-1 < 0 or dp[res[rowIndex][colIndex-1]]:
                    # Have to change direction
                    direction = 3
                else:
                    colIndex-=1
                    start+=1
            elif direction == 3:
                #Travelling up
                if rowIndex-1 < 0 or dp[res[rowIndex-1][colIndex]]:
                    # Have to change direction
                    direction = 0
                else:
                    rowIndex-=1
                    start+=1
        res[rowIndex][colIndex] = start
        return res

            