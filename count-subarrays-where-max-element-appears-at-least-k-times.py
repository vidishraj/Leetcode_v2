class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # prefixCount = {}
        # n = len(nums)
        # maxNum = max(nums)
        # curr = 0
        # for i in range(n):
        #     prefixCount[i] = curr
        #     if nums[i]==maxNum:
        #         curr+=1
        # prefixCount[n] = curr
        # # print(prefixCount)
        # res = 0
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         total = prefixCount[j] - prefixCount[i]
        #         # print(i, j-1, total)
        #         if total>=k:
        #             res+=1

        max_num = max(nums)
        count = 0
        res = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == max_num:
                count += 1
            
            while count >= k:
                if nums[l] == max_num:
                    count -= 1
                l += 1
            
            res += l
        return res