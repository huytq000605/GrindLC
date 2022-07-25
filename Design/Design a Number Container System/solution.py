from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.idx_to_num = dict()
        self.num_to_idx = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.idx_to_num:
            num = self.idx_to_num[index]
            self.num_to_idx[num].remove(index)
        self.idx_to_num[index] = number
        self.num_to_idx[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.num_to_idx or not len(self.num_to_idx[number]):
            return -1
        return self.num_to_idx[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
