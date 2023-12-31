class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last_seen = [-1 for _ in range(26)]
        offset = ord('a')
        result = -1
        for i, c in enumerate(s):
            c = ord(c) - offset
            if last_seen[c] != -1:
                result = max(result, i - last_seen[c] - 1)
            else:
                last_seen[c] = i
        return result
