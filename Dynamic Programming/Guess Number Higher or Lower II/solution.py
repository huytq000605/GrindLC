class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def guess(start, end):
            if start >= end:
                return 0
            result = math.inf
            for root in range(start, end):
                left = guess(start, root - 1)
                right = guess(root + 1, end)
                result = min(result, max(left + root, right + root))
            return result
        return guess(1, n)