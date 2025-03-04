class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # Possibilities are that the new interval can eat up multiple intervals
        # First we need to first the interval that it belongs after -> newStartTime<endTime 
        # Once we reach this case, we have options, it can be before, it can be together -> interval becomes 
        # part of new or new becomes part of interval
        
        # Before-> if newendTime<startTime
        # newinterval become part -> if startTime<=newStartTime and newEndTime<=endTime
        # interval becomes part -> if newStartTime>=startTime and endTime<=newEndTime
        spliceIdx = None
        newStartTime, newEndTime = newInterval
        for idx, interval in enumerate(intervals):
            startTime, endTime = interval 
            if newStartTime<=endTime:
                spliceIdx = idx
                break

        if spliceIdx is None:
            intervals.append(newInterval)
            return intervals
        
        # Before case
        res = []
        startTime, endTime = intervals[spliceIdx]
        if newEndTime<startTime:
            res = intervals[:spliceIdx]+[newInterval]+intervals[spliceIdx:]
            return res
        
        # newInterval becomes part 
        if startTime<=newStartTime and newEndTime<=endTime:
            return intervals
        
        res = intervals[:spliceIdx]
        
        newStartTime = min(newStartTime, intervals[spliceIdx][0])
        while spliceIdx<len(intervals) and (newEndTime>=intervals[spliceIdx][1] or intervals[spliceIdx][0]<=newEndTime):
            newEndTime = max(intervals[spliceIdx][1], newEndTime)
            spliceIdx+=1
        res = res+ [[newStartTime, newEndTime]] +intervals[min(len(intervals),spliceIdx):]
        return res
    