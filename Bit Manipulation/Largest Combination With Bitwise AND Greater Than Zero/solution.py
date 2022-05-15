class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        result = 0
        n = len(candidates)
        for i in range(32):
            cur = 0
            for can in candidates:
                if (1<<i) & can != 0:
                    cur += 1
            result = max(result, cur)
        return result