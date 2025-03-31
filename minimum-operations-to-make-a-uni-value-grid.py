class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Not possible if all are not multiples of the number x 
        # If all are, make a list of the number 
        # Sort and find the median 
        numsInList = [item for inner in grid for item in inner]
        numsInList.sort()
        if len(set(val%x for val in numsInList)) > 1: return -1 # impossible

        if len(grid)==1 and len(grid[0])==1:
            return 0
        # for num in numsInList:
        #     if num%x!=0:
        #         return -1
        idx = 0
        if len(numsInList)%2==0:
            idx = len(numsInList)//2 -1
        else:
            idx = len(numsInList)//2
        itemToMatch = numsInList[idx]
        res = 0
        for num in numsInList:
            res+=(abs(num-itemToMatch))/x
        return int(res)