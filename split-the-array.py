class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        itemDict={}
        for num in nums:
            if itemDict.get(num) is None:
                itemDict[num]=1
            else:
                itemDict[num]+=1
        for count in itemDict.values():
            if count>2:
                return False
        return True