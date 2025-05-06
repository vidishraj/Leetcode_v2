class MinStack:
    minHeap: list
    countDict: dict
    stack: list
    def __init__(self):
        self.stack = []
        self.minHeap = []
        self.countDict = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minHeap, val)
        self.countDict[val]+=1

    def pop(self) -> None:
        val = self.stack.pop()
        self.countDict[val]-=1 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minHeap)==0:
            return Non
        while self.minHeap and self.countDict[self.minHeap[0]]==0:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()