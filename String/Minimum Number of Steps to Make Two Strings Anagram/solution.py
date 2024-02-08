class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter = [0 for _ in range(26)]
        offset = ord('a')
        for c in s:
            counter[ord(c) - offset] += 1
        for c in t:
            counter[ord(c) - offset] -= 1
        return sum(counter)
