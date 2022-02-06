class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.set = set()
        self.is_flip = False

    def fix(self, idx: int) -> None:
        if self.is_flip:
            if idx in self.set:
                self.set.remove(idx)
        else:
            self.set.add(idx)

    def unfix(self, idx: int) -> None:
        if self.is_flip:
            self.set.add(idx)
        else:
            if idx in self.set:
                self.set.remove(idx)

    def flip(self) -> None:
        self.is_flip = not self.is_flip

    def all(self) -> bool:
        if self.is_flip:
            return len(self.set) == 0 
        else:
            return len(self.set) == self.size

    def one(self) -> bool:
        if self.is_flip:
            return len(self.set) != self.size
        else:
            return len(self.set) >= 1

    def count(self) -> int:
        if self.is_flip:
            return self.size - len(self.set)
        else:
            return len(self.set)

    def toString(self) -> str:
        result = ""
        if self.is_flip:
            for i in range(self.size):
                if i not in self.set:
                    result += "1"
                else:
                    result += "0"
        else:
            for i in range(self.size):
                if i in self.set:
                    result += "1"
                else:
                    result += "0"
        return result
            


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()