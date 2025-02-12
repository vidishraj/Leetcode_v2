class Solution:
    def twoEggDrop(self, n: int) -> int:
        solutionList=[i for i in range(1,46)]
        runningCount=0
        for index,item in enumerate(solutionList):
            runningCount+=item
            if(runningCount>=n):
                return index+1