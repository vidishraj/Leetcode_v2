class Solution:
    def findNewList(self, nums):
        heap = []
        for i in range(1, len(nums)):
            s = nums[i-1]+nums[i]
            heap.append((s, i))

        heapq.heapify(heap)
        smallestSum, index  = heapq.heappop(heap)
        return nums[:index-1]+[smallestSum]+nums[index+1:]

    def checkIncreasing(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1]>nums[i]:
                return False
        return True
        
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        numRef = nums
        while True:
            if self.checkIncreasing(numRef):
                return res
            numRef = self.findNewList(numRef)
            res+=1
        return res