class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 1, len(arr)-2
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] > arr[mid+1]:
                end = mid
            else:
                start = mid + 1
        return start
