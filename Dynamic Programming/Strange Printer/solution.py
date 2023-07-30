class Solution:
    def strangePrinter(self, s: str) -> int:
        ps = ""
        for c in s:
            if ps and ps[-1] == c: continue
            ps += c
            
        @cache
        def dfs(start, end):
            if start == end:
                return 1
            result = end - start + 1
            for split in range(start, end):
                result = min(result, dfs(start, split) + dfs(split+1, end))
            if ps[start] == ps[end]:
                result -= 1
            return result
        
        return dfs(0, len(ps) - 1)
