class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        chars = set(s)
        result = 0
        counter = defaultdict(int)
        start = 0
        for i in range(len(s)):
            counter[s[i]] += 1
            while counter[s[i]] > 2:
                counter[s[start]] -= 1
                if counter[s[start]] == 0: counter.pop(s[start])
                start += 1
            result = max(result, i - start + 1)
        return result
