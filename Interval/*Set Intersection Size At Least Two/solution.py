class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # We are sure that the next interval will always be on the right
        intervals.sort(key = lambda interval: (interval[1], -interval[0]))
        arr = []
        for a, b in intervals:
            # The next intervals are always on the right, so we greedy choose rightest point
            
            # Nothing can be reused
            if not arr or a > arr[-1]:
                arr.extend([b-1, b])
            # Only the last can be reused
            elif a > arr[-2]:
                arr.append(b)
        return len(arr)