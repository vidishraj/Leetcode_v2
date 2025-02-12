class Solution(object):
    def minMaxDifference(self, num):
        """
        map first value that is not a 9 to a 9 to get the max value and min the first value to get the min value
        :type num: int
        :rtype: int
        """
        maxDigit=""
        minDigit=num.__str__()[0]
        minValue=int(num.__str__().replace(minDigit, '0'))
        maxValue=num
        for digit in num.__str__():
            if digit != '9':
                maxDigit=digit
                break

        if maxDigit!="":
            maxValue=int(num.__str__().replace(maxDigit,'9'))
        return maxValue-minValue
