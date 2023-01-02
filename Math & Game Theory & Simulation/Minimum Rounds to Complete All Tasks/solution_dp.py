class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        result = 0
        @cache
        def dfs(num):
            if num == 0:
                return 0
            if num < 2:
                return math.inf
            return 1 + min(dfs(num - 2), dfs(num - 3))
        for freq in counter.values():
            turns = dfs(freq)
            if turns == math.inf:
                return -1
            result += turns
        return result