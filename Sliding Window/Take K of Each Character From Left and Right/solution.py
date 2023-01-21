class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter(s)
        for c in "abc":
            if counter[c] < k:
                return -1
        prefix = [0, 0, 0]
        idx = {"a": 0, "b": 1, "c": 2}
        suffix = [counter["a"], counter["b"], counter["c"]]
        n = len(s)
        j = 0
        result = n
        for i in range(n):
            while j < n and prefix[idx[s[j]]] + suffix[idx[s[j]]] -1 >= k:
                suffix[idx[s[j]]] -= 1
                j += 1
            result = min(i + (n - j), result)
            prefix[idx[s[i]]] += 1
        return result
            

