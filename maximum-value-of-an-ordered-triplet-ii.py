class Solution:
        def maximumTripletValue(self, A: List[int]) -> int:
            res = maxa = maxab = 0
            for a in A:
                res = max(res, maxab * a)
                maxab = max(maxab, maxa - a)
                maxa = max(maxa, a)
            return res