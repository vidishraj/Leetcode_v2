class Router:
    # Queue to store incoming packets, drop when memory limit exceeds
    # dict to store if the packet exists
    itemDict: defaultdict
    q: deque
    packetCount: int
    memoryLimit: int
    
    def __init__(self, memoryLimit: int):
        self.itemDict = defaultdict(bool)
        self.q = deque()
        self.packetCount = 0
        self.memoryLimit = memoryLimit
        self.destMap = defaultdict(SortedList)
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        itemTup = (source, destination, timestamp)
        if self.itemDict[itemTup]:
            # duplicate
            return False
        else:
            if self.packetCount>=self.memoryLimit:
                # Memory limit exceed, remove the oldest
                oldPacket =  self.q.popleft()
                oldsrc, olddst, oldtime = oldPacket
                self.destMap[olddst].discard(oldtime)
                self.itemDict[oldPacket] = False
                self.packetCount-=1
            self.packetCount+=1
            self.q.append(itemTup)
            self.destMap[destination].add(timestamp)
            self.itemDict[itemTup] = True
            return True
                
            

    def forwardPacket(self) -> List[int]:
        if len(self.q)==0:
            return []
        itemTup = self.q.popleft()
        src, dst, time = itemTup
        self.itemDict[itemTup] = False
        self.packetCount-=1
        self.destMap[dst].discard(time)
        return list(itemTup)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destMap[destination]
        left = timestamps.bisect_left(startTime)
        right = timestamps.bisect_right(endTime)
        return right-left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)