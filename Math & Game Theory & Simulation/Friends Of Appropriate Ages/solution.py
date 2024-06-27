
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        result = 0
        for x in range(1, 121):
            for y in range(1, x+1):
                if y <= 0.5 * x + 7: continue
                if x == y:
                    result += counter[x] * (counter[x] - 1)
                else:
                    result += counter[x] * counter[y]
        return result
