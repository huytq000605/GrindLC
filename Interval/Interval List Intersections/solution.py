class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        result = []
        while i < len(f) and j < len(s):
            f_start, f_end = f[i]
            s_start, s_end = s[j]
            left = max(f_start, s_start)
            right = min(f_end, s_end)
            if left <= right:
                result.append([left, right])
                
            if f_end <= s_end:
                i += 1
            else:
                j += 1
        return result
                