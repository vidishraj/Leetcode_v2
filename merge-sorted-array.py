class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return nums1
        else:
            lastZero = m+n-1
            lastM = m-1
            lastN = n-1 
            for i in range(m+n-1, -1, -1):
                if len(nums2)==0:
                    return nums1
                if lastM>=0 and nums1[lastM]>=nums2[lastN]:
                    nums1[lastZero] = nums1[lastM]
                    nums1[lastM] = 0
                    lastM-=1
                else:
                    nums1[lastZero] = nums2[lastN]
                    nums2.pop()
                    lastN-=1
                    
                lastZero-=1
        return nums1 
                
                    
            
        
        