class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        dq = deque()
        max_dp = 0
        power.sort()
        result = 0
        for p in power:
            if dq and dq[-1][0] == p:
                dq[-1][1] += p
            else:
                while dq and dq[0][0] + 2 < p:
                    max_dp = max(max_dp, dq.popleft()[1])
                dq.append([p, p + max_dp])
            result = max(result, dq[-1][1])
        return result
