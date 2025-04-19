class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0 
        def sumOfDigits(strI):
            res = 0
            for item in strI:
                res+= int(item)
            return res

        for i in range(low, high+1):
            strI = str(i)
            midPoint = len(strI)//2
            if len(strI)%2==0:
                firstHalf =strI[midPoint:]
                secondHalf = strI[:midPoint]
                if sumOfDigits(firstHalf)==sumOfDigits(secondHalf):
                    res+=1
        return res

