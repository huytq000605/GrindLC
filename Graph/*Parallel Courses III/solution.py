class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        requiredPrev = [[] for i in range(n)]
        for rel in relations:
            requiredPrev[rel[1] - 1].append(rel[0] - 1)
        @lru_cache(None)
        def learn(course):
            result = time[course]
            bonus = 0
            for required in requiredPrev[course]:
                bonus = max(bonus, learn(required))
            return result + bonus
        minimumTime = 0
        for course in range(n):
            minimumTime = max(minimumTime, learn(course))
        return minimumTime