from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.list = deque()
        self.sortedlist = SortedList()
        self.m = m
        self.k = k
        self.sum = 0
        self.first_k = 0
        self.last_k = 0

    def addElement(self, num: int) -> None:
        k, m = self.k, self.m
        
        idx = self.sortedlist.bisect_left(num)
        if idx <= k - 1:
            self.first_k += num
            if len(self.list) >= k:
                self.first_k -= self.sortedlist[k-1]
        
        if idx >= len(self.list) - k + 1:
            self.last_k += num
            if len(self.list) >= k:
                self.last_k -= self.sortedlist[len(self.list) - k]
        
        self.list.append(num)
        self.sortedlist.add(num)
        self.sum += num
        
        if len(self.list) == m + 1:
            pop = self.list.popleft()
            idx = self.sortedlist.index(pop)
            self.sum -= pop
            if idx <= k - 1:
                self.first_k -= pop
                self.first_k += self.sortedlist[k]
            if idx >= m + 1 - k:
                self.last_k -= pop
                self.last_k += self.sortedlist[m-k]
            self.sortedlist.remove(pop)

    def calculateMKAverage(self) -> int:
        k, m = self.k, self.m
        if len(self.list) < m:
            return -1
        return (self.sum - self.first_k - self.last_k) // (m - 2 * k)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()