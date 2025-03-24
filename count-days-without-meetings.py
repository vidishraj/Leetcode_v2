class Solution:

    @staticmethod 
    def mergeMeetings(meetings):
        mergedMeetings = [meetings[0]]
        next = 1
        while next<len(meetings):
            currStart, currEnd = mergedMeetings[-1]
            nextStart, nextEnd = meetings[next]
            if currStart == nextStart: # Case [3,4] and [3,5]-> Make both 3,5
                mergedMeetings[-1] = (nextStart,nextEnd)
                next+=1
            elif currStart<nextStart and currEnd>nextEnd: # Case [3,6], [4,5]
                # Essentially do nothing , next belong inside 
                next+=1
            elif currStart<nextStart and nextStart == currEnd: # Case [1,3] [3, 10]
                mergedMeetings[-1] = (currStart, nextEnd)
                next+=1
            elif currStart<nextStart and nextStart<currEnd and currEnd<=nextEnd: # Case [3, 5], [4, 8]
                mergedMeetings[-1] = (currStart, nextEnd)
                next+=1
            else:
                mergedMeetings.append(meetings[next])
                next+=1
        return mergedMeetings
        
    @staticmethod 
    def countBusyDays(meetings):
        busyDays = 0 
        for meeting in meetings:
            busyDays+=meeting[1]-meeting[0]+1
        return busyDays

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # merge intervals and then count
        # Sort, iterate, merge, move on 
        # To merge-> Compare first index-> Can be equal but 1 is greater , can be greater than 0 but less than 1, can be greater than 0 and greater than 1 (no merge)
        meetings.sort()
        mergedMeetings = self.mergeMeetings(meetings)
        return days - self.countBusyDays(mergedMeetings)
