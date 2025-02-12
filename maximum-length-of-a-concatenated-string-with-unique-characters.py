class Solution:
    wordList:list
    maximumL:int

    def checkString(self, currentString, index):

        def compareString(str1, str2):
            return len(set(str1).intersection(str2))==0
            
        def indexCheck(index):
            return len(set(index)) == len(index)
            
        if index<len(self.wordList):
            if indexCheck(self.wordList[index]) and compareString(currentString, self.wordList[index]):
                # String2 is unique and doesnt exist in existing string
                self.checkString(currentString+self.wordList[index], index+1)
                self.checkString(currentString, index+1)
            else:
                # String2 is not unique or already exists in currentString.
                # Move on without it
                self.checkString(currentString, index+1)
        else:
            if self.maximumL<len(currentString):
                self.maximumL = len(currentString)
        
        return
    def maxLength(self, arr: List[str]) -> int:
        # At every point, add it or not add it 
        self.wordList = arr
        self.maximumL = 0 
        self.checkString("", 0 )
        return self.maximumL
