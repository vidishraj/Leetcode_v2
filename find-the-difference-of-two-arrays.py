class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        num1 not present in num2 and num2 not present in num1
        """
        
        num1Dict = {}
        num2Dict = {}
        for num in nums1:
            num1Dict[num] = True
        for num in nums2:
            num2Dict[num] = True
        dict1Keys = list(num1Dict.keys())
        dict2Keys = list(num2Dict.keys())
        return [[num for num in dict1Keys if num not in num2Dict], [num for num in dict2Keys if num not in num1Dict]]
        
        