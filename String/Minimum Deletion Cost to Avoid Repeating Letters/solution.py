from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        currentWord = s[0]
        currentCost = cost[0]
        result = 0
        for index, word in enumerate(s):
            if index == 0:
                continue
            if word == currentWord:
                result += min(currentCost, cost[index])
                currentCost = max(currentCost, cost[index])
                continue
            currentCost = cost[index]
            currentWord = word
        return result
            