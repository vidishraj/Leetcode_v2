class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        end = (2 ** n)-1
        if n==1:
            if nums[0]=="0":
                return "1"
            return "0"
        start = 0
        endIdx = len(nums)-1
        nums.sort()
        def convertToBinary(num):
            nonlocal n
            binaryString = ""
            while num>0:
                rem = math.floor(num%2)
                binaryString = str(rem)+binaryString
                num= math.floor(num/2)
            return (n-len(binaryString))*"0"+binaryString
        def convertToNum(binary):
            startExp = 0
            res=0
            for i in range(len(binary)-1, -1, -1):
                if binary[i]=="1":
                    res+=2**startExp
                startExp+=1
            return res
                

        while start<end:
            frontItem = nums[start]
            backItem = nums[endIdx]

            if start!=convertToNum(frontItem):
                if start==0:
                    return n*"0"
                return convertToBinary(start)

            if end!=convertToNum(backItem):
                return convertToBinary(end)
            start+=1
            end-=1
        