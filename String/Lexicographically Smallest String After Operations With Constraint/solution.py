class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        result = ""
        for c in s:
            d1 = ord(c) - ord('a')
            d2 = ord('z') - ord(c) + 1
            if k >= min(d1, d2): 
                k -= min(d1, d2)
                result += 'a'
            else:
                result += chr(ord(c) - k)
                k = 0
        return result
                
                
