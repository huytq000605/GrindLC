class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        start = 0
        end = len(self.d[key]) - 1
        d = self.d[key]
        while start < end:
            mid = start + math.ceil((end - start + 1) // 2)
            if d[mid][1] > timestamp:
                end = mid - 1
            else:
                start = mid
        if d[start][1] <= timestamp:
            return d[start][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
