class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        if (len(arr) == 3):
            return 1
        low = 0
        high = len(arr) - 1
        mid = int((high - low) / 2 + low)
        while low < high:
            if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
                return mid
            if arr[mid - 1] > arr[mid]:
                high = mid
            if arr[mid + 1] > arr[mid]:
                low = mid
            mid = int((high - low) / 2 + low)
        return mid