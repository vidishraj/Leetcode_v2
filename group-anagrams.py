class Solution(object):
    
    def getUniqueId(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)
    
    def groupAnagrams(self, nums):
        result=[]
        itemDict = {}
        for num in nums:
            key = self.getUniqueId(num)
            if itemDict.get(key) is not None:
                itemDict[key].append(num)
            else:
                itemDict[key]=[num]
        result.extend(itemDict.values())
        return result