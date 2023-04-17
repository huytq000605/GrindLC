class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        n = len(candies)
        result = [False for _ in range(n)]
        for i in range(n):
            if candies[i] + extraCandies >= mx:
                result[i] = True
        return result
