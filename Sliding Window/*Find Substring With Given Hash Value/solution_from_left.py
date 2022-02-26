class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        current_hash = 0
        
        @cache
        def idx(l):
            return ord(l) - ord("a") + 1
        
        more = 1
        for i in range(k):
            plus = idx(s[i]) * more
            more *= power
            # more %= modulo
            current_hash += plus
            # current_hash %= modulo
        if current_hash % modulo == hashValue:
            return s[:k]
        more //= power
        for i in range(k, n):
            current_hash -= idx(s[i-k])
            current_hash //= power
            plus = idx(s[i]) * more
            current_hash += plus
            if current_hash % modulo == hashValue:
                return s[i-k+1:i+1]
            
        return ""