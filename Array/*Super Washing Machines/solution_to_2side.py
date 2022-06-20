class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        if sum(machines) % n:
            return -1
        target = sum(machines) // n
        # Like #979. Distribute Coins in Binary Tree
        # to_right[i] = how many dresses it need to pass to the right
        to_right = [0 for i in range(n)]
        # to_left[i] = how many dresses it need to pass to the left
        to_left = [0 for i in range(n)]
        result = 0
        for i, machine in enumerate(machines):
            if i > 0:
                to_right[i] = to_right[i-1] + machine - target
            else:
                to_right[i] = machine - target
            
            result = max(result, to_right[i])
        
        for i in range(n-1, -1, -1):
            machine = machines[i]
            if i < n-1:
                to_left[i] = to_left[i+1] + machine - target
            else:
                to_left[i] = machine - target
            result = max(result, to_left[i], to_left[i] + to_right[i])
        return result