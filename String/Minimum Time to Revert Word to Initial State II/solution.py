class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        l, r = 0, 0
        n = len(word)
        # Can also using KMP and search from the last
        z = [0 for _ in range(n)]
        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < n and word[i + z[i]] == word[z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l = i
                r = i + z[i]

        for i in range(k, n, k):
            if z[i] >= n-i:
                return i // k
        return math.ceil(n/k)
