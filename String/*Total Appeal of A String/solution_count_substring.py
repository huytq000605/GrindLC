class Solution:
    def appealSum(self, s: str) -> int:
        last = [-1 for i in range(26)]
        n = len(s)
        result = 0
        total = 0
        # total = how many substrings
        for i, l in enumerate(s):
            c = ord(l) - ord('a')
						# i + 1 - (last[c] + 1) is number of substrings that doesnt have s[i] but now they have it
            total += i + 1 - (last[c]+1)
            last[c] = i
            result += total
        return result