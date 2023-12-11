class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        cur = -1
        for num in arr:
            if num != cur:
                cur = num
                count = 0
            count += 1
            if count > n / 4:
                return cur
        return -1
