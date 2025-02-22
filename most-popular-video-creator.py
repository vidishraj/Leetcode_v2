class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        # Goal is to find [] of most popular creator-> their most viewed with lexographically smallest id
        # Use one max heap to save the view counts individusally for a creator
        # use one max heap to save aggr view counts
        viewMaxHeapMap = defaultdict(list)
        for i in range(len(creators)):
            creator= creators[i]
            creatorId = ids[i]
            creatorView = views[i]
            heapq.heappush(viewMaxHeapMap[creator], (-1*creatorView, creatorId))
        creatorDict = defaultdict(int)
        for i in range(len(creators)):
            creatorDict[creators[i]]+=views[i]
        sortedView = sorted(creatorDict, key = creatorDict.get, reverse = True)
        highestView = creatorDict[sortedView[0]]
        highestC = []
        for k in sortedView:
            if creatorDict[k]==highestView:
                highestC.append(k)
        res = []
        for creator in highestC:
            res.append([creator,viewMaxHeapMap[creator][0][-1]])
        return res