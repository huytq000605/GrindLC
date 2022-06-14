class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mapping_dict = defaultdict(dict)
        for u, v in mappings:
            mapping_dict[u][v] = True
        m, n = len(s), len(sub)
        for i in range(m-n+1):
            j = 0
            valid = True
            for l in range(n):
                if s[i + l] == sub[j + l]:
                    continue
                if sub[j+l] in mapping_dict and s[i+l] in mapping_dict[sub[j+l]]:
                    continue
                valid = False
                break
            if valid:
                return True
        return False