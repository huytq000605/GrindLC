class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        if sum(machines) % n:
            return -1
        target = sum(machines) // n
				# balance is number of dresses need to move through each machine
        balance = 0
        result = 0
        for machine in machines:
            balance += machine - target
						# there maybe some cases the machine has to pass the dresses to 2 side
						# so (machine - target) will be bigger than balance
            result = max(result, abs(balance), machine - target)
        return result