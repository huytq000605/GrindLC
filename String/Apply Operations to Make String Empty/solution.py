class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counter = Counter(s)
        result = ""
        mx = max(counter.values())
        for c in s[::-1]:
            if counter[c] == mx:
                result += c
                counter[c] = 0
        return result[::-1]
