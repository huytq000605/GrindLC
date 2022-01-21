class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        balance = 0
        n = len(gas)
        start = 0
        for i in range(n):
            balance += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if balance < 0:
                balance = 0
                start = i + 1
        if total < 0:
            return -1
        return start