class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        counter_top = [0 for i in range(7)]
        counter_btm = [0 for i in range(7)]
        same = [0 for i in range(7)]
        
        for i in range(n):
            counter_top[tops[i]] += 1
            counter_btm[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                same[tops[i]] += 1
        
        result = math.inf
        for i in range(7):
            if counter_top[i] + counter_btm[i] - same[i] == n:
                result = min(result, min(counter_top[i] - same[i], counter_btm[i] - same[i]))
        if result == math.inf:
            return -1
        return result