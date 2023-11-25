class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        min_first = max(0, n - 2 * limit)
        max_first = min(n, limit)
        for first in range(min_first, max_first + 1):
            remaining = n - first
            min_second = max(0, remaining - limit)
            max_second = min(limit, remaining)
            result += max_second - min_second + 1
        return result
