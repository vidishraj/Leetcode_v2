class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        numDic=dict()
        res=[]
        for num in nums1:
            numDic[num[0]]=num[1]
        for num in nums2:
            if num[0] not in numDic.keys():
                res.append(num)
            else:
                numDic[num[0]]+=num[1]
        for key in numDic.keys():
            res.append([key,numDic[key]])
        return sorted(res, key=lambda x: x[0])