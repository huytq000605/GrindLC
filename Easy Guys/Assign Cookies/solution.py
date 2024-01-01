class Solution:
    def findContentChildren(self, gs: List[int], cookies: List[int]) -> int:
        gs.sort()
        cookies.sort()
        g, c = 0, 0
        result = 0
        while g < len(gs) and c < len(cookies):
            while c < len(cookies) and cookies[c] < gs[g]:
                c += 1
            if c < len(cookies):
                result += 1
            c += 1
            g += 1
        return result 
