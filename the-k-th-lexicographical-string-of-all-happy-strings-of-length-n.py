class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        currSol = ""
        solFound = 0
        res = ""
        itemList = ['a', 'b','c']
        def backtrack():
            nonlocal n, k, currSol, solFound, itemList, res
            if solFound>k:
                return
            lastChar = currSol[-1]
            if len(currSol) == n:
                solFound+=1
                if solFound==k:
                    res = currSol
                return
            for i in range(3):
                item = itemList[i]
                if item!=lastChar:
                    currSol+=item
                    backtrack()
                    currSol = currSol[:-1]
            return

        for i in range(3):
            item = itemList[i]
            currSol+=item
            backtrack()
            currSol = ""
        return res