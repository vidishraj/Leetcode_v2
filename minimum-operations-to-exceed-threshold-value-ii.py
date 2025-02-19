import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # I guess we can use a heap?
        ops = 0
        heap = []

        for num in nums:
            # Insert items 
            heapq.heappush(heap, num)
        while heap[0]<k and len(heap)>=2:
            ops+=1
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            resNum = min(x,y)*2+max(x,y)
            heapq.heappush(heap, resNum)
        # print(heap)
        return ops