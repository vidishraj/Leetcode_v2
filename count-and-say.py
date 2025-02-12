class Solution:
    def reverse(self, s):
        result = ""
        for i in range(len(s) - 1, -1, -1):
            result += s[i]
        return result

    def recHelper(self, s):
        resultString = ""
        s = self.reverse(s)
        currentChar = s[-1]
        s = s[0:-1]
        currentCount = 1
        while len(s) > 0:
            #print(s, resultString)
            char = s[-1]
            s = s[0:-1]
            if char == currentChar:
                currentCount += 1
            else:
                resultString += str(currentCount) + currentChar
                currentCount = 1
                currentChar = char

        resultString += str(currentCount) + currentChar
        return resultString

    def countAndSay(self, n: int) -> str:
        solution = "1"
        while n>1:
            solution=self.recHelper(solution)
            n-=1
        #print(solution)
        return solution