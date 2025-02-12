class Solution:
    def maximumTripletValue(self, nums: list[int]):
        minValue=0
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    tripletValue=(nums[i]-nums[j])*nums[k]
                    if minValue< tripletValue and tripletValue>=0:
                        minValue=tripletValue
        return minValue