class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        dq = deque()
        result = 0
        costs = 0
        start = 0
        for end in range(n):
            charge, cost = chargeTimes[end], runningCosts[end]
            while dq and dq[-1][1] <= charge:
                dq.pop()
            dq.append((end, charge))
            costs += cost
            while dq and dq[0][1] + (end - start + 1) * costs > budget:
                if start == dq[0][0]:
                    dq.popleft()
                costs -= runningCosts[start]
                start += 1
            result = max(result, end - start + 1)
        return result
