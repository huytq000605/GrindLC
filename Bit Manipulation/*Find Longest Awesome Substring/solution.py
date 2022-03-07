class Solution:
    def longestAwesome(self, s: str) -> int:
        current = 0
        seen = dict()
        seen[0] = -1
        result = 0 
        for idx, d in enumerate(s):
            bit = 1 << int(d)
            current ^= bit
            if current == 0:
                result = max(result, idx + 1)
            else:
                for i in range(26):
                    target = 1 << i
                    if target ^ current in seen:
                        result = max(result, idx - seen[target ^ current])
            if current not in seen:
                seen[current] = idx
        return result