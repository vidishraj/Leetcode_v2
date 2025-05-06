class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
            First check if it is possible. 
            Then check if its better to do it in the bottom or the top 
            Then do the rotations.
        """

        # How to check if it is possible? 
        # There should be at least one number that is equal to the length of dominoes
        numCount= defaultdict(lambda: [0,0])
        possible = defaultdict(bool)
        n = len(tops)
        for item in tops:
            numCount[item][1]+=1
        for item in bottoms:
            numCount[item][0]+=1
        common = [tops[0],bottoms[0]]
        for i in range(1,n):
            curr = [tops[i], bottoms[i]]
            newC = []
            for j in range(len(common)):
                if curr[0]==common[j] or curr[1]==common[j]:
                    newC.append(common[j])
            common = newC
        if len(common)==0:
            return -1
        res = float('inf')
        for item in numCount:
            topCount, bottomCount = numCount[item]
            if topCount+bottomCount>=n and item in common:
                res = min(res, min(n-topCount, n-bottomCount))
        return res
        