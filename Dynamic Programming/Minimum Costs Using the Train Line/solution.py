class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        last_express, last_regular = expressCost, 0
        result = [0 for _ in range(n)]
        for i in range(n):
            new_express = min(last_regular + expressCost + express[i], last_express + express[i])
            new_regular = min(last_regular + regular[i], last_express + regular[i])
            last_express, last_regular = new_express, new_regular
            result[i] = min(new_express, new_regular)
        return result
        
