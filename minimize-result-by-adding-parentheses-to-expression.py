class Solution:
    s:str
    plusIdx:int
    minVal:int
    minStr:str
    # When remaking strings, we need to remember, 0->currentIdx+1(to include ) + "required" + currentIdx+1->len(s)
    def recChecks(self, idx, currStr, oDropped):
        # print(idx, currStr, oDropped)
        if idx >= self.plusIdx and not oDropped:
            # We didn't drop the bracket in time
            return 
        if idx>=len(self.s)+2:
            return
        def evalStr(newStr:str):
            if newStr[-1]=="*":
                newStr  = newStr[:-1]
            if newStr[0]=="*":
                newStr  = newStr[1:]
            try:
                evaluation = eval(newStr)
            except:
                evaluation = float('inf')
            if self.minVal>evaluation:
                self.minVal = evaluation
                self.minStr = newStr
            
        if idx<=self.plusIdx-1:
            # Drop a openBracket here 
            if not oDropped:
                # print("Open", currStr, idx)
                newStr = currStr[:idx]+"*("+currStr[idx:]
                self.recChecks(idx+1, newStr[:], True)
            self.recChecks(idx+1, currStr[:], oDropped)
            
        elif idx>=self.plusIdx+1 and oDropped:
            # Don't drop an closingBracket here
            self.recChecks(idx+1, currStr[:], oDropped)
            # Drop a closingBracket here and evaluate
            newStr = currStr[:idx+2]+")*"+currStr[idx+2:]
            evalStr(newStr)
            return
        else:
            # print("HERE")
            self.recChecks(idx+1, currStr[:], oDropped)


    def minimizeResult(self, expression: str) -> str:
        # We want to check all possibilites of button brackets on both sides of the +
        # Can use backtracking of sorts
        self.s = expression
        self.plusIdx = expression.index("+")
        self.minVal = float('inf')
        self.recChecks(0, expression[:], False)
        self.minStr  = self.minStr.replace("*",'')
        return self.minStr