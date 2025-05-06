from typing import List

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        totalVal = 0
        seenRows = set()
        seenCols = set()
        remainingRows = n
        remainingCols = n

        # Process queries in reverse order
        for queryType, index, val in reversed(queries):
            if queryType == 0:  # Row operation
                if index not in seenRows:
                    totalVal += val * remainingCols  # Affect only unmarked columns
                    seenRows.add(index)
                    remainingRows -= 1
            else:  # Column operation
                if index not in seenCols:
                    totalVal += val * remainingRows  # Affect only unmarked rows
                    seenCols.add(index)
                    remainingCols -= 1

        return totalVal
