class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        # make a hashmap and keep the following two values-> The first time when a number appeared and the index at
        # which its degree becomes the frequency. When at the end we have the hashmap with two values in the array.
        # We subtract and find their value.
        frequency = 0
        countDict = {}
        for num in nums:
            if countDict.get(num):
                countDict[num] += 1
                if frequency < countDict[num]:
                    frequency = countDict[num]
            else:
                countDict[num] = 1
                if frequency==0:
                    frequency=1
        if frequency==1: return 1
        indexHash = {}
        leastLength = len(nums)
        for index, num in enumerate(nums):
            if indexHash.get(num) is not None:
                indexHash[num]['frequency'] += 1
                #print(indexHash)
                if indexHash[num]['frequency'] == frequency:
                    indexHash[num]["freqIndex"] = index
                    if leastLength > index - indexHash[num]['startIndex'] + 1:
                        leastLength = index - indexHash[num]['startIndex'] + 1
            else:
                indexHash[num] = {
                    "startIndex": index,
                    "endIndex": "",
                    "frequency": 1
                }
        return leastLength