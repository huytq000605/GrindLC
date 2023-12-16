class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out = set()
        for u, v in paths:
            out.add(u)
        for u, v in paths:
            if v not in out:
                return v
        return ""
