class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        operations=0
        initialSum = -1
        i = 0 
        while(i<len(nums)):
            # print(initialSum)
            if(i+1<len(nums)):
                if initialSum==-1:
                    initialSum=nums[i]+nums[i+1]
                    operations+=1
                else:
                    if nums[i]+nums[i+1]!=initialSum:
                        return operations
                    else:
                        operations+=1
            i+=2    
        return operations