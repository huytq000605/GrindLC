class Solution:
    def minWindow(self, s: str, t: str) -> str:
        require = Counter(t)
        start = 0
        result = (-1, -1)
        for i, c in enumerate(s):
            require[c] -= 1
            while start < len(s) and require[s[start]] < 0:
                require[s[start]] += 1
                start += 1
            if all([require[c] <= 0 for c in require.keys()]):
                if result[1] == -1 or (i-start+1) < (result[1] - result[0] + 1):
                    result = (start, i+1)
        return s[result[0]:result[1]]
