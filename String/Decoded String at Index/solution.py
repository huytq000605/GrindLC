class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        for i, c in enumerate(s):
            if c.isdigit():
                length *= int(c)
            else:
                length += 1
            if length >= k:
                break
        
        k -= 1
        while True:
            if s[i].isdigit():
                length //= int(s[i])
                k %= length
            else:
                if k == length - 1:
                    return s[i]
                length -= 1
            i -= 1
        return s[i]
            
            
