class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        la, lb = len(a), len(b)
        idxs = []
        for i in range(n-lb+1):
            if s[i:i+lb] == b:
                idxs.append(i)
        result = []
        j = 0
        for i in range(n-la+1):
            while j < len(idxs) and i - k > idxs[j]:
                j += 1
            if s[i:i+la] == a:
                if j < len(idxs) and abs(idxs[j] - i) <= k:
                    result.append(i)
        return result
