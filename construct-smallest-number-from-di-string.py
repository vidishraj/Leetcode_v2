class Solution:
    def smallestNumber(self, pattern: str) -> str:
        numDict = {}
        for i in range(1, 10):
            numDict[i] = 0
        res = ""
        finalRes= ""
        resFound = False
        def backtrack(currIdx):
            nonlocal res, numDict, pattern, resFound, finalRes
            lastNum = int(res[-1])
            if resFound:
                return
            if currIdx == len(pattern):
                finalRes = res[:]
                resFound=True
                return 
            if pattern[currIdx] == "D":
                for i in range(1, lastNum):
                    if numDict[i] == 0 :
                        res +=str(i)
                        numDict[i]+=1
                        backtrack(currIdx+1)
                        numDict[i]-=1
                        res = res[:-1]

            else:
                for i in range(lastNum+1, 10):
                    if numDict[i] == 0 :
                        res+=str(i)
                        numDict[i]+=1
                        backtrack(currIdx+1)
                        numDict[i]-=1
                        res = res[:-1]
            return 
        for i in range(1,10):
            res +=str(i)
            numDict[i]+=1
            backtrack(0)
            if not resFound:
                numDict[i]-=1
                res = ""
            else:
                return finalRes
        return  finalRes