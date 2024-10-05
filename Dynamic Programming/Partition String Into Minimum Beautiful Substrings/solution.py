class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        se = set()
        num = 1
        for i in range(8):
            se.add(num)
            num *= 5
        
        @cache
        def dfs(i, mask):
            if i >= len(s):
                if mask == 0: return 0
                else: return math.inf
            if mask == 0 and s[i] == "0":
                return math.inf
            mask = (mask << 1) + int(s[i])
            result = dfs(i+1, mask)
            if mask in se:
                result = min(result, 1 + dfs(i + 1, 0))
            return result
        
        result = dfs(0, 0)
        if result == math.inf:
            return -1
        return result
                
