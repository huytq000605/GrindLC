class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        result = 0
        s = 0
        for i in range(1, n+1):
            if i not in banned and s + i <= maxSum:
                result += 1
                s += i
        return result
