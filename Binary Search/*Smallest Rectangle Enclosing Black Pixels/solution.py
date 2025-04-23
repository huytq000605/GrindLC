class Solution:
    def minArea(self, image: List[List[str]], r: int, c: int) -> int:
        m, n = len(image), len(image[0])
        def black_col(col):
            for r in range(m):
                if image[r][col] == '1': return True
            return False    
        def black_row(row):
            return "1" in image[row]
        def search_min(lo, hi, fn):
            while lo < hi:
                mi = lo + (hi - lo) // 2
                
                if fn(mi):
                    hi = mi
                else:
                    lo = mi + 1
            return lo   
        def search_max(lo, hi, fn):
            while lo < hi:
                mi = lo + (hi - lo + 1) // 2
                if fn(mi):
                    lo = mi
                else:
                    hi = mi-1
            return lo
        
        min_col = search_min(0, c, black_col)
        max_col = search_max(c, n-1, black_col)
        min_row = search_min(0, r, black_row)
        max_row = search_max(r, m-1, black_row)
        return (max_row-min_row+1) * (max_col-min_col+1)


