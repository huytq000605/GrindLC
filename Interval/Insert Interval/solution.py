class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        s, e = newInterval
        for i in intervals:
            if i[1] < s:
                left.append(i)
            elif i[0] > e:
                right.append(i)
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return [*left, [s, e], *right]
