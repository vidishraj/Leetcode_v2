class Solution:
    
    def sumOfDigits(self, num):
        strNum = str(num)
        sumIs=0
        for number in strNum:
            sumIs+=int(number)
        return sumIs
    
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumofDigits=self.sumOfDigits(x)
        if x % sumofDigits==0:
            return sumofDigits
        return -1
        