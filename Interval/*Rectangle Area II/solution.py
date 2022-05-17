class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        x_values = set()
        for x1, y1, x2, y2 in rectangles:
            x_values.add(x1)
            x_values.add(x2)
        x_values = sorted(x_values)
        x_map = {v:i for i, v in enumerate(x_values)}
        
        ys = []
        for x1, y1, x2, y2 in rectangles:
            ys.append((y1, x1, x2, 1))
            ys.append((y2, x1, x2, -1))
        
        ys.sort()
        count = [0 for i in range(len(x_values))]
        result = 0
        x_area = 0
        prev_y = 0

        for y, x1, x2, sign in ys:
            result += (y - prev_y) * x_area
            result %= 10**9 + 7
            prev_y = y
            
            for x in range(x_map[x1], x_map[x2]):
                count[x] += sign
            
            x_area = 0
            for x in range(len(x_values) - 1):
                if count[x] > 0:
                    x_area += x_values[x + 1] - x_values[x]
        
        return result