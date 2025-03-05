class Solution:
    def coloredCells(self, n: int) -> int:
        # It is a math question 
        # 1-> 1 n=1
        # 2-> 5 n=2
        # 3-> 13  n=3 
        # 4-> 25
        # eq seems to be n * n + (n-1) ** 2 
        return (n*n)+((n-1)**2)