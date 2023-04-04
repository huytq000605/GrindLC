class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cost = [i+1 for i in range(26)]
        n = len(chars)
        for i in range(n):
            idx = ord(chars[i]) - ord('a')
            cost[idx] = vals[i]
        result = 0
        cur = 0
        for c in s:
            cur += cost[ord(c) - ord('a')]
            result = max(result, cur)  
            if cur < 0:
                cur = 0
        return result
