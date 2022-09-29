class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        start, end = 0, n - k
        while start < end:
            mid = start + (end - start) // 2
            # compare starting of the other choices to ending of this choice
            if arr[mid+k] - x < x - arr[mid]:
                start = mid + 1
            else:
                end = mid
        return arr[start:start+k]
