class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        # Write a method to fill grid 
        # Method take starting column, ending column, startingRow, endingRow, startingNumber
        size = 2 ** N
        matrix = [[0 for _ in range(size)] for _ in range(size)]

        def fillGrid(r, c, n, start):
            if n == 0:
                matrix[r][c] = start
                return

            half = 2 ** (n - 1)
            count = half * half

            fillGrid(r, c + half, n - 1, start)                  
            fillGrid(r + half, c + half, n - 1, start + count)   
            fillGrid(r + half, c, n - 1, start + 2 * count)      
            fillGrid(r, c, n - 1, start + 3 * count)             

        fillGrid(0, 0, N, 0)
        return matrix