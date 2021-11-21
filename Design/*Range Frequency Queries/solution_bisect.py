import bisect

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        d = dict()
        for i, num in enumerate(arr):
            if num not in d: 
                d[num] = []
            d[num].append(i)
        self.d = d

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.d: return 0
        d = self.d[value]
        start = bisect.bisect_left(d, left)
        end = bisect.bisect_right(d, right)
        
        return end - start


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)