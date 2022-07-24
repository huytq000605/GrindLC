class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
            return "Flush"
        counter = Counter(ranks)
        max_rank = 0
        for val in counter.values():
            max_rank = max(val, max_rank)
        if max_rank >= 3:
            return "Three of a Kind"
        elif max_rank == 2:
            return "Pair"
        else:
            return "High Card"
