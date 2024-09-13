class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False for _ in range(n)]
        pq = []
        for i, num in enumerate(nums):
            heappush(pq, (num, i))
        score = 0
        while pq:
            num, i = heappop(pq)
            if marked[i]: continue
            if i > 0: marked[i-1] = True
            if i < n-1: marked[i+1] = True
            score += num
        return score
