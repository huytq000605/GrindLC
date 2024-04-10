class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = deque()
        for card in sorted(deck, reverse = True):
            if result:
                result.appendleft(result.pop())
            result.appendleft(card)
        return result
