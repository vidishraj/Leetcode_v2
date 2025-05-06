class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        globalItemDict = defaultdict(int)
        for collection in responses:
            itemDict= defaultdict(bool)
            for item in collection:
                itemDict[item] = True
            for item in itemDict:
                globalItemDict[item]+=1
        maxCount = float('-inf')
        for item in list(globalItemDict.values()):
                maxCount = max(maxCount, item)
        topItems = []
        for item in globalItemDict:
            if globalItemDict[item]==maxCount:
                topItems.append(item)
        topItems.sort()
        return topItems[0]