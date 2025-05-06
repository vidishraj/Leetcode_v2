class Solution:
    largestPrime: int
    primeDict: dict

    def isPrime(self, num):
        if num>10:
            if self.primeDict.get(num) is not None:
                self.primeDict[num] += 1
                return
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            self.primeDict[num] = 1
            return True

    def reset(self, current, mat):
        i = current[0]
        j = current[1]
        currentNum = ""
        return i, j, currentNum

    def travelInAllDirections(self, mat: list[list[int]], current: tuple):
        i, j, currentNum = self.reset(current, mat)
        # Travel north
        while i > -1:
            currentNum += str(mat[i][j])
            self.isPrime(int(currentNum))
            i -= 1
        i, j, currentNum = self.reset(current, mat)
        # travel south
        while i < len(mat):
            currentNum += str(mat[i][j])
            self.isPrime(int(currentNum))
            i += 1
        i, j, currentNum = self.reset(current, mat)
        # Travel east
        while j < len(mat[0]):
            currentNum += str(mat[i][j])
            self.isPrime(int(currentNum))
            j += 1
        i, j, currentNum = self.reset(current, mat)
        # Travel west
        while j > -1:
            currentNum += str(mat[i][j])
            self.isPrime(int(currentNum))
            j -= 1
        i, j, currentNum = self.reset(current, mat)
        # Travel north-east
        while i > -1 and j < len(mat[0]):
            currentNum += str(mat[i][j])
            self.isPrime(int(currentNum))
            i -= 1
            j += 1
        i, j, currentNum = self.reset(current, mat)
        # Travel south-east
        while i < len(mat) and j < len(mat[0]):
            currentNum += str(mat[i][j])
            self.isPrime(int(currentNum))
            i += 1
            j += 1
        i, j, currentNum = self.reset(current, mat)
        # Travel south-west
        while i < len(mat) and j > -1:
            currentNum += str(mat[i][j])
            self.isPrime(int(currentNum))
            i += 1
            j -= 1
        i, j, currentNum = self.reset(current, mat)
        # Travel north-west
        while i > -1 and j > -1:
            currentNum += str(mat[i][j])
            self.isPrime(int(currentNum))
            i -= 1
            j -= 1

    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        # maybe write code to 
        self.primeDict = {}
        self.largestPrime = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                self.travelInAllDirections(mat, tuple([i, j]))
        self.primeDict = dict(sorted(self.primeDict.items(), key=lambda item: item[1], reverse=True))
        keys=list(self.primeDict.keys())
        if len(keys)==0:
            return -1
        currentMax=self.primeDict[keys[0]]
        totalMax= keys[0]
        for item in self.primeDict:
            if self.primeDict[item]==currentMax:
                if item>totalMax:
                    totalMax=item
            else:
                break
        return totalMax
