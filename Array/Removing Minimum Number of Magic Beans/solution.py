class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        total = sum(beans)
        result = math.inf
        for i in range(len(beans)):
            after = beans[i] * (n-i)
            result = min(result, total - after)
        return result