class Solution:
    @staticmethod
    def findVerticalIntervals( rectangles):
        intervals = [[item[1], item[3]] for item in rectangles]
        intervals.sort()
        return intervals

    @staticmethod
    def findHorizontalIntervals( rectangles):
        intervals = [[item[0], item[2]] for item in rectangles]
        intervals.sort()
        return intervals
    @staticmethod
    def checkMerge(intervals):
        # We mrge when there is a rectangle inside or there is a overlap. We do not merge for 
        # Ending and starting being the same 
        mergedIntervals = [tuple(intervals[0])]
        next = 1
        while next<len(intervals):
            currStart, currEnd = mergedIntervals[-1][0], mergedIntervals[-1][1]
            nextStart, nextEnd = intervals[next][0], intervals[next][1]
            if nextStart<currEnd and nextEnd>=currEnd: #merge when overlap 
                mergedIntervals[-1] = (currStart, nextEnd)
                next+=1
            elif nextStart<currEnd and nextEnd<currEnd:
                next+=1
            else:
                mergedIntervals.append(tuple(intervals[next]))
                next+=1
        return len(mergedIntervals)>2

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Essentially just a merge interval question 
        verticalIntervals = self.findVerticalIntervals(rectangles)
        horizontalIntervals = self.findHorizontalIntervals(rectangles)
        return self.checkMerge(verticalIntervals) or self.checkMerge(horizontalIntervals)