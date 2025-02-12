import copy
class Solution:
    maximumVal:int
    grid:list
    def travel(self, collectedGold, i, j):
        def checkMaximum():
            if self.maximumVal<collectedGold:
                self.maximumVal=collectedGold
        if  0<=i<len(self.grid) and 0<=j<len(self.grid[0]):
            # We are in range
            # if i==4 and j==4:
            #     print(collectedGold, visited)
            if self.grid[i][j]==0:
                checkMaximum()
                return
            else:
                collectedGold+=self.grid[i][j]
                curr = self.grid[i][j]
                self.grid[i][j] = 0
                self.travel(collectedGold, i+1, j)
                self.travel(collectedGold, i-1, j)
                self.travel(collectedGold, i, j+1)
                self.travel(collectedGold, i, j-1)
                self.grid[i][j] = curr
                checkMaximum() 
        
            

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # Have to check every possibility
        self.maximumVal = 0
        self.grid = grid
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item>0:
                    self.travel(0, i, j)
        return self.maximumVal