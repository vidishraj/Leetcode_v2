class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        #Remove the first occurence from the right 
        lowestNum = 0
        for index, num in enumerate(number):
            if num == digit:
                removedNum = int(number[0:index]+number[index+1:len(number)])
                if lowestNum<removedNum:
                    lowestNum = removedNum
        return str(lowestNum)