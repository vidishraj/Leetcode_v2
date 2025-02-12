class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        count=0
        for hour in hours:
            if hour>=target:
                count+=1
                
        return count