class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(profit)
        jobs = sorted([(difficulty[i], profit[i]) for i in range(n)])
        i, p, result = 0, 0, 0
        for w in sorted(worker):
            while i < n and jobs[i][0] <= w:
                p = max(p, jobs[i][1])
                i += 1
            result += p
        return result
