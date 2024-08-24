class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1: return str(int(n) - 1)
        half = n[:(len(n) + 1) // 2]
        candidates = [
            "9" * (len(n) - 1)
        ]
        for d in range(-1, 2):
            prefix = str(int(half) + d)
            if len(n) % 2: candidate = prefix + prefix[:-1][::-1]
            else: candidate = prefix + prefix[::-1]
            candidates.append(candidate)
        candidates.append('1' + '0' * (len(n) - 1) + '1')
        diff = math.inf
        result = ""
        for cand in candidates:
            d = abs(int(cand) - int(n))
            if d and d < diff:
                diff = d
                result = cand
        return result
