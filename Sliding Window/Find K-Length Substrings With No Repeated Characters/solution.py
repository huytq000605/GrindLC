class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        counter = [0 for _ in range(26)]
        offset = ord('a')
        result = 0
        for i in range(len(s)):
            if i - k >= 0:
                counter[ord(s[i-k]) - offset] -= 1
            counter[ord(s[i]) - offset] += 1
            if i >= k-1 and max(counter) < 2: result += 1
        return result
