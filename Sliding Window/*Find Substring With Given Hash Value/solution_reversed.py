class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        current_hash = 0
        s = s[::-1]
        result = []
        
        @cache
        def idx(l):
            return ord(l) - ord("a") + 1
        
        more = 1
        for i in range(k):
            current_hash *= power
            current_hash %= modulo
            more *= power
            more %= modulo
            current_hash += idx(s[i])
            current_hash %= modulo
        
        if current_hash == hashValue:
            result.append(k-1)
        
        for i in range(k, n):
            current_hash *= power
            current_hash %= modulo
            
            current_hash -= (idx(s[i-k]) * more) % modulo
            current_hash = (current_hash + modulo) % modulo
            
            current_hash += idx(s[i])
            current_hash %= modulo
            if current_hash == hashValue:
                result.append(i)

        last = result.pop()
        return s[last-k+1:last+1][::-1]