class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        result = 0
        for freq in counter.values():
            if freq == 1:
                return -1
            # if freq % 3 == 0: turns = freq // 3
            # if freq % 3 == 1 => freq = 3m + 1 = 3(m-1) + 2 + 2
            # if freq % 3 == 2 => freq = 3m + 2
            turns = freq // 3 + 1
            if freq % 3 == 0:
                turns -= 1
            result += turns
        return result