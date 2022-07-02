
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        MOD = 10**9+7

        max_horizontal = 0
        prev = 0
        for cut in verticalCuts:
            max_horizontal = max(max_horizontal, cut - prev)
            prev = cut
        max_horizontal = max(max_horizontal, w - prev)

        max_vertical = 0
        prev = 0
        for cut in horizontalCuts:
            max_vertical = max(max_vertical, cut - prev)
            prev = cut
        max_vertical = max(max_vertical, h - prev)

        return max_horizontal * max_vertical % MOD
