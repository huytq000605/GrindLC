class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        t, s = list(target), list(stamp)
        result = []
        n, m = len(t), len(s)

        def check(i):
            changed = False
            for j in range(m):
                if t[i + j] == '?': continue
                if t[i + j] != s[j]: return False
                changed = True
            if changed:
                t[i:i + m] = ['?'] * m
                result.append(i)
            return changed

        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= check(i)
        for l in t:
            if l != "?":
                return []
        return result[::-1]