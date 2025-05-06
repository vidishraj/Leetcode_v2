class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # We will iterate in that patter and then sort the array that is formed
        # We will join this into a res string
        # Reiterate and change values

        # Start from bottom left and go to top Right
        n = len(grid)
        if n==1:
            return grid
        row = n-1 
        col = 0
        sortR = ""
        # bottom left done
        while row>-1:
            tempRow = row
            tempCol = 0
            diagVal = []
            while tempRow<n and tempCol<n:
                diagVal.append(grid[tempRow][tempCol])
                tempRow+=1
                tempCol+=1
            diagVal.sort(reverse = True)
            sortR += "".join("," + str(item) for item in diagVal)
            row-=1
        row = 0
        col = 1
        while col<n:
            tempRow = 0
            tempCol = col
            diagVal = []
            while tempRow<n and tempCol<n:
                diagVal.append(grid[tempRow][tempCol])
                tempRow+=1
                tempCol+=1
            diagVal.sort()
            sortR += "".join( "," + str(item) for item in diagVal)
            col+=1
        # print(sortR)
        currIndex = 0
        row = n-1
        sortR = sortR.split(",")
        sortR = sortR[1:]
        while row>-1:
            tempRow = row
            tempCol = 0
            while tempRow<n and tempCol<n:
                val = sortR[currIndex]
                grid[tempRow][tempCol] = int(val)
                currIndex+=1
                tempRow+=1
                tempCol+=1
            row-=1
        col = 1
        while col<n:
            tempRow = 0
            tempCol = col
            while tempRow<n and tempCol<n:
                val = sortR[currIndex]
                grid[tempRow][tempCol] = int(val)
                tempRow+=1
                tempCol+=1
                currIndex+=1
            col+=1
        return grid