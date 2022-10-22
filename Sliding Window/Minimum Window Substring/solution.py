class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = defaultdict(int)
        for c in t:
            required[c] += 1
        result = ""
        start = 0
        n = len(s)
        def check():
            for v in required.values():
                if v > 0:
                    return False
            return True
        for i, c in enumerate(s):
            required[s[i]] -= 1
            while start < len(s) and required[s[start]] < 0:
                required[s[start]] += 1
                start += 1
            if check() and (len(result) == 0 or len(result) > (i - start + 1)):
                result = s[start:i+1]
            
        return result
