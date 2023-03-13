class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        prev = 0
        for num in arr:
            if num - prev - 1 >= k:
                return prev + k
            else:
                k -= (num - prev - 1)
                prev = num
        return arr[-1] + k
