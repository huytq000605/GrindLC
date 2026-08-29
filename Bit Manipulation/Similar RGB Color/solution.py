class Solution:
    def similarRGB(self, color: str) -> str:
        def similar(c):
            v = int(c, 16)
            d = v // 17
            result = d
            for i in (-1, 1):
                if d + i < 0: continue
                if abs(v - 17*(d+i)) < abs(v - 17*d):
                    result = d+i
            return hex(result)[2:]*2

        return f"#{similar(color[1:3])}{similar(color[3:5])}{similar(color[5:])}"
