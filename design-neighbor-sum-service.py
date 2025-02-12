class NeighborSum:
    grid:list
    n:int
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)

    def findKey(self, value):
        for outIndex, item in enumerate(self.grid):
            for innerIndex, innerItem in enumerate(item):
                if innerItem == value:
                    return outIndex, innerIndex
                
    def adjacentSum(self, value: int) -> int:
        rowIndex, colIndex = self.findKey(value)
        indices = [(rowIndex+1, colIndex), (rowIndex-1, colIndex), (rowIndex, colIndex-1),(rowIndex, colIndex+1)]
        adjSum = 0
        for index in indices:
            if index[0]<self.n and index[0]>-1 and index[1]<self.n and index[1]>-1:
                adjSum+=self.grid[index[0]][index[1]]
        return adjSum
    def diagonalSum(self, value: int) -> int:
        rowIndex, colIndex = self.findKey(value)
        indices = [(rowIndex+1, colIndex+1), (rowIndex-1, colIndex+1), (rowIndex+1, colIndex-1),(rowIndex-1, colIndex-1)]
        adjSum = 0
        for index in indices:
            if index[0]<self.n and index[0]>-1 and index[1]<self.n and index[1]>-1:
                adjSum+=self.grid[index[0]][index[1]]
        return adjSum


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)