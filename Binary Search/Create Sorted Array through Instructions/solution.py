from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = SortedList()
        result = 0
        for num in instructions:
            left = arr.bisect_left(num)
            right = arr.bisect_right(num)
            result += min(len(arr) - right, left)
            result %= (10**9+7)
            arr.add(num)
        return result