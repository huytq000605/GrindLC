class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        result= 1
        
        hBars.sort()
        max_diff_h = 1
        h_start = 1
        h_idx = 0
        while True:
            h_end = h_start + 1
            while h_idx < len(hBars) and h_end == hBars[h_idx]:
                h_idx += 1
                h_end += 1
            max_diff_h = max(max_diff_h, h_end - h_start)
            if h_idx >= len(hBars):
                break
            h_start = hBars[h_idx] - 1
            
        vBars.sort()
        max_diff_v = 1
        v_start = 1
        v_idx = 0
        while True:
            v_end = v_start + 1
            while v_idx < len(vBars) and v_end == vBars[v_idx]:
                v_idx += 1
                v_end += 1
            max_diff_v = max(max_diff_v, v_end - v_start)
            if v_idx >= len(vBars):
                break
            v_start = vBars[v_idx] - 1
        
        return min(max_diff_v, max_diff_h) ** 2
        
