class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        s = 0
        for i in range(n):
            each = round((target - s) / n)
            if each < arr[i]:
                return each
            n -= 1
            s += arr[i]
        return arr[-1]
