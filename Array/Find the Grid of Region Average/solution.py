class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        intensities = [[[0, 0] for _ in range(n)] for _ in range(m)]
        # consider each center region
        for cr in range(1, m-1):
            for cc in range(1, n-1):
                is_region = True
                # consider each cell in region
                for r, c in [(cr, cc), (cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)]:
                    if not is_region:
                        break
                    # consider each adj cell of each cell
                    for d in [-1, 1]: # 3
                        nr, nc = r + d, c + d
                        if cr-1 <= nr <= cr+1 and abs(image[r][c] - image[nr][c]) > threshold:
                            is_region = False
                            break
                        if cc-1 <= nc <= cc+1 and abs(image[r][c] - image[r][nc]) > threshold:
                            is_region = False
                            break
                            
                if is_region:
                    s = 0
                    for r in range(cr-1, cr+2):
                        for c in range(cc-1, cc+2):
                            s += image[r][c]
                    for r in range(cr-1, cr+2):
                        for c in range(cc-1, cc+2):
                            intensities[r][c][0] += s // 9
                            intensities[r][c][1] += 1
        
        return [[intensities[r][c][0] // intensities[r][c][1] if intensities[r][c][1] > 0 else image[r][c] for c in range(n)] for r in range(m)]
                    
                    
