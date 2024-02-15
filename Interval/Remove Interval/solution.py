class Solution:
    def removeInterval(self, intervals: List[List[int]], remove: List[int]) -> List[List[int]]:
        i = 0
        result = []
        for a, b in intervals:
            overlap_a, overlap_b = max(a, remove[0]), min(b, remove[1])
            # not overlap
            if overlap_a > overlap_b:
                result.append([a, b])
                continue
            
            a1, b1 = a, min(remove[0], b)
            if a1 < b1: result.append([a1, b1])
            
            a2, b2 = max(remove[1], a), b
            if a2 < b2: result.append([a2, b2])
        return result
