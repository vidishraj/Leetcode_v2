class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        def checkPartition(arr):
            if not 2<=len(arr)<=3:
                return False
            if len(arr)==2:
                if arr[0]==arr[1]:
                    return True
            else:
                if arr[0]==arr[1]==arr[2]:
                    return True
                if arr[2]-arr[1]==1 and arr[1]-arr[0]==1:
                    return True
            return False
        @lru_cache(maxsize=100000)
        def backtrack(startingNum, endingNum):
            if endingNum-startingNum>3:
                return False
            # print(startingNum, endingNum)
            if startingNum==len(nums):
                return True
            if startingNum>len(nums) or endingNum>len(nums):
                return False
            if checkPartition(nums[startingNum:endingNum]):
                # Parition works
                return backtrack(endingNum, endingNum+1) or backtrack(startingNum, endingNum+1)
            else:
                #Parition doesn't work
                return backtrack(startingNum, endingNum+1)
            
        return backtrack(0,1)