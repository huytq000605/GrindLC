class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def height(a, b):
            h = 0
            while True:
                if a < h + 1: break
                h += 1
                a -= h
                if b < h + 1: break
                h += 1
                b -= h
            return h
        return max(height(red, blue), height(blue, red))

        
