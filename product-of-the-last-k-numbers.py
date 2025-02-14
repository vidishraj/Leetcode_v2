class ProductOfNumbers:
    dp:dict
    runningMul: int
    currIndex: int
    zeroIndex : int

    def __init__(self):
        self.dp = {}
        self.currIndex = 0
        self.runningMul = 1
        self.zeroIndex = -1
        
    def add(self, num: int) -> None:
        if num == 0 :
            num = 1
            self.zeroIndex = self.currIndex + 1
        self.runningMul *= num
        self.currIndex+=1
        self.dp[self.currIndex] = self.runningMul

    def getProduct(self, k: int) -> int:
        idxToCheck = self.currIndex-k
        if self.zeroIndex!=-1 and self.zeroIndex>idxToCheck:
            return 0
        if idxToCheck == 0:
            return self.runningMul
        productTillThere = self.dp.get(idxToCheck)
        if productTillThere == 0:
            return 0
        return int(self.runningMul / productTillThere)
        
