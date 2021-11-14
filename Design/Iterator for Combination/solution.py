class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.arr = []
        def dfs(idx, curr):
            if len(curr) == combinationLength:
                self.arr.append(curr)
                return
            if idx >= len(characters):
                return
            seen = set()
            for i in range(idx, len(characters)):
                if characters[i] in seen:
                    continue
                seen.add(characters[i])
                dfs(i + 1, curr + characters[i])
        dfs(0, "")
        self.idx = 0
        

    def next(self) -> str:
        combi = self.arr[self.idx]
        self.idx += 1
        return combi

    def hasNext(self) -> bool:
        return self.idx < len(self.arr)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()