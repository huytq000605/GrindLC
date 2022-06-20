class Solution:
    def sumScores(self, s: str) -> int:
        def z_function(s):
            l, r = 0, 0
            n = len(s)
            z = [0 for i in range(n)]
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                else:
                    while i + z[i] < n and s[i + z[i]] == s[z[i]]:
                        z[i] += 1
                    if i + z[i] - 1 > r:
                        l, r = i, i + z[i] - 1
            return z
        return sum(z_function(s)) + len(s)