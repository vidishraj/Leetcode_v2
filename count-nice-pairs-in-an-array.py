class Solution:
    def reverse(self, num: int):
        numInString = str(num)
        numInReverse = ""
        for letter in range(len(numInString) - 1, -1, -1):
            numInReverse += numInString[letter]
        return int(numInReverse)

    def countNicePairs(self, nums: list):
        reversedList = []
        countNicePairs = 0
        differenceHash = {}
        for word in nums:
            if(word<10):
                reversedList.append(word)
            else:
                reversedList.append(self.reverse(word))
        for index in range(0, len(nums)):
            if differenceHash.get(nums[index] - reversedList[index]):
                countNicePairs += differenceHash.get(nums[index] - reversedList[index])
                differenceHash[nums[index] - reversedList[index]] += 1
            else:
                differenceHash[nums[index] - reversedList[index]] = 1
        return countNicePairs%(10**9+7)
