class Excel:

    def __init__(self, m: int, n: str):
        n = ord(n) - ord('A') + 1
        self.grid = [[0 for _ in range(n)] for _ in range(m)]
        self.sums = [[None for _ in range(n)] for _ in range(m)]
        self.calculated = dict()

    def set(self, row: int, column: str, val: int) -> None:
        r = row-1
        c = ord(column) - ord('A')
        self.grid[r][c] = val
        self.sums[r][c] = None

    def _get(self, r, c):
        if (r, c) in self.calculated: return self.calculated[(r,c)]
        if self.sums[r][c] is None:
            return self.grid[r][c]
        result = 0
        for pos, freq in self.sums[r][c].items():
            result += self._get(pos[0], pos[1]) * freq
        self.calculated[(r, c)] = result
        return result

    def get(self, row: int, column: str) -> int:
        r = row-1
        c = ord(column) - ord('A')
        self.calculated = {}
        return self._get(r, c)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        r = row-1
        c = ord(column) - ord('A')
        self.sums[r][c] = self.parse(numbers)
        return self.get(row, column)

    def parse(self, strs):
        res = defaultdict(int)
        for s in strs:
            if ":" not in s:
                res[(int(s[1:]) - 1, ord(s[0]) - ord('A'))] += 1
            else:
                s1, s2 = s.split(":")
                rc1 = (int(s1[1:]) - 1, ord(s1[0]) - ord('A'))
                rc2 = (int(s2[1:]) - 1, ord(s2[0]) - ord('A'))
                for r in range(rc1[0], rc2[0]+1):
                    for c in range(rc1[1], rc2[1] + 1):
                        res[(r, c)] += 1
        return res
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
