from collections import defaultdict

class Solution:
    def __init__(self):
        self.dp = {}

    def splitNum(self, givenString: str, startIndex: int, currSum: int, parent: int) -> bool:
        # Memoization key: (startIndex, currSum)
        key = (startIndex, currSum)
        if key in self.dp:
            return self.dp[key]

        # Base case: reached the end of the string
        if startIndex == len(givenString):
            return currSum == parent

        result = False
        for endIndex in range(startIndex, len(givenString)):
            numStr = givenString[startIndex:endIndex + 1]

            # Skip numbers with leading zeros (except "0" itself)
            if len(numStr) > 1 and numStr[0] == "0":
                continue

            num = int(numStr)
            if currSum + num <= parent:
                # Recursively try splitting further
                if self.splitNum(givenString, endIndex + 1, currSum + num, parent):
                    result = True
                    break  # No need to check further if we already found a valid split

        self.dp[key] = result  # Store result in memoization
        return result

    def punishmentNumber(self, n: int) -> int:
        totalSum = 0

        for i in range(1, n + 1):
            self.dp = {}  # Reset memoization for each number
            squaredNumber = str(i * i)

            if self.splitNum(squaredNumber, 0, 0, i):
                totalSum += int(squaredNumber)

        return totalSum
