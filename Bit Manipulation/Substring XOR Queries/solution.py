class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        have = dict()
        n = len(s)
        for i in range(n):
            cur = 0
            for j in range(i, min(i+31, n)):
                cur *= 2
                cur += int(s[j])
                if cur not in have:
                    have[cur] = [i, j]
                if j == i and s[j] == "0":
                    break
        result = []
        for a, b in queries:
            q = a ^ b
            if q not in have:
                result.append([-1, -1])
            else:
                result.append(have[q])
        return result
