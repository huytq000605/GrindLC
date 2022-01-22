class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        current = 0
        result = 0
        for c in cost:
            if current == 2:
                current = 0
                continue
            result += c
            current += 1
            
        return result