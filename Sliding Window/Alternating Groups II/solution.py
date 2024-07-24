class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        prev = -1
        l = 0
        result = 0
        for i in range(n + k - 1):
            if colors[i%n] != prev:
                l += 1
            else:
                l = 1
            prev = colors[i%n]
            if l >= k:
                result += 1
        return result
