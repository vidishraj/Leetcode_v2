class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0 for i in range(k)]
        prev = Counter()
        for num in nums:
            numMod = num % k
            curr = Counter()
            curr[numMod]+=1
            res[numMod]+=1

            for seen in prev:
                newMod = (seen *numMod)%k
                curr[newMod]+= prev[seen]
                res[newMod]+= prev[seen]
            prev = curr
        return res
        
        # TOO  SLOW
        # products = []
        # n = len(nums)
        # runningP = 1
        # res = [0 for i in range(k)]
        # for i in range(n):
        #     prod = 1
        #     for j in range(i, n):
        #         prod = (prod * nums[j])%k
        #         res[prod]+=1
        # return res
        