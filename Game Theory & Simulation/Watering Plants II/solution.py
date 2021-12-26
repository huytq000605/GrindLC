class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        i = 0
        j = n - 1
        curA = capacityA
        curB = capacityB
        result = 0
        while i < j:
            if curA < plants[i]:
                result += 1
                curA = capacityA
            curA -= plants[i]
            if curB < plants[j]:
                result += 1
                curB = capacityB
            curB -= plants[j]
            i += 1
            j -= 1
            
        if i == j:
            cur = max(curA, curB)
            if cur < plants[i]:
                result += 1
        return result