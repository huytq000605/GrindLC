class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        result = 0
        for i in range(k):
            result += max(0, happiness[i] - i)
        return result
