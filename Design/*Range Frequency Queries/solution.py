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
        start = 0
        end = len(d) - 1
        while(start < end):
            mid = start + ((end - start) // 2)
            if d[mid] < left:
                start = mid + 1
            else:
                end = mid
        if d[start] < left or d[start] > right:
            return 0
        left = start
        
        end = len(d) - 1
        while start < end:
            mid = start + ceil((end - start + 1) / 2)
            if d[mid] > right:
                end = mid - 1
            else:
                start = mid
        if d[start] > right or d[start] < left:
            return 0
        right = start
        return right - left + 1


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)