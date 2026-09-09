class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n - 999) + \
            max(0, n - 999_999) + \
            max(0, n - 999_999_999) + \
            max(0, n - 999_999_999_999) + \
            max(0, n - 999_999_999_999_999)
