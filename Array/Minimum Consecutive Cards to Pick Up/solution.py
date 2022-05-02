class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        idxs = dict()
        result = math.inf
        for i, num in enumerate(cards):
            if num not in idxs:
                idxs[num] = i
            else:
                result = min(i - idxs[num] + 1, result)
                idxs[num] = i
        if result == math.inf:
            return -1
        return result