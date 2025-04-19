class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)
        dp = []
        maxCount = 1
        for i in range(len(nums)-1, -1, -1):
            count[nums[i]]+=1
            maxCount = max(maxCount, count[nums[i]])
            dp.append(maxCount)
        dp = list(reversed(dp))
        res = 0
        i = 0
        while i<=len(nums)-3:
            el1,el2, el3 = dp[i], dp[i+1], dp[i+2]
            if el1==1 and el2==1 and el3==1:
                return res
            res+=1
            i+=3
        for j in range(i, len(dp)):
            if dp[i]>1:
                res+=1
                break
        return res