class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        prefix = 0
        result = 0
        print(satisfaction)
        for s in satisfaction:
            if (s >= 0) or (s < 0 and prefix + s > 0):
                prefix += s
                result += prefix
        return result
        
