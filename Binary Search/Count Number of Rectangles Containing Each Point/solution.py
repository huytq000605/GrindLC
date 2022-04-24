class Solution(object):
    def countRectangles(self, rectangles, points):
        rects = defaultdict(list)
        for l, h in rectangles:
            rects[h].append(l)
        for key in rects.keys():
            rects[key].sort()
        
        result = [0 for i in range(len(points))]
        for i, (x, y) in enumerate(points):
            for yo in range(y, 101):
                if yo not in rects:
                    continue
                start = 0
                end = len(rects[yo]) - 1
                while start < end:
                    mid = start + (end - start) // 2
                    if rects[yo][mid] >= x:
                        end = mid
                    else:
                        start = mid + 1
                if rects[yo][start] >= x:
                    result[i] += len(rects[yo]) - start
        return result