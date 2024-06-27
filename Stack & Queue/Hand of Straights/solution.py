import collections

# Technically, this solution is still O(NlogN + N + N)
# Because of the constraint, so each element will be walk through at most once in the for loop, and once in the while loop
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = collections.Counter()
        for card in hand:
            freq[card] += 1
        
        for card in sorted(freq.keys()):
            if freq[card] == 0:
                continue
            need = freq[card]
            size = 0
            while size < groupSize:
                if freq[card] < need:
                    return False
                freq[card] -= need
                card += 1
                size += 1
        return True
