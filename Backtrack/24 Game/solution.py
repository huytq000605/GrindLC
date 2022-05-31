class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs():
            nonlocal cards
            if len(cards) == 1:
                if abs(cards[0] - 24) < 0.01:
                    return True
                return False
            for i in range(len(cards)):
                for j in range(i+1, len(cards)):
                    a, b = cards[i], cards[j] 
                    next_nums = [a+b, a-b, b-a, a*b]
                    if b > 0.01: next_nums.append(a/b)
                    if a > 0.01: next_nums.append(b/a)
                    cards.pop(j)
                    cards.pop(i)
                    for next_num in next_nums:
                        cards.append(next_num)
                        if dfs():
                            return True
                        cards.pop()
                    cards.insert(i, a)
                    cards.insert(j, b)
            return False
        return dfs()