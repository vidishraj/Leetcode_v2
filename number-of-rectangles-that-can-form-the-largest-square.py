class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxSq = defaultdict(int)
        larg =  float('-inf')
        for i, rec in enumerate(rectangles):
            l,w = rec[0], rec[1]
            maxSq[min(l,w)] +=1
            larg = max(larg, min(l,w))
        return maxSq[larg]
        