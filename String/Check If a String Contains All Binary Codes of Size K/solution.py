class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        seen = set()
        binary = 0
        for i in range(k):
            binary <<= 1
            binary |= int(s[i])
        seen.add(binary)
        
        for i in range(k, len(s)):
            binary <<= 1
            binary &= ~(1<<k)
            binary |= int(s[i])
            seen.add(binary)
            if len(seen) == (1 << k):
                return True
        return False