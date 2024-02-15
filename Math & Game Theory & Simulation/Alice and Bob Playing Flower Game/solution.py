class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # total number of flowers is odd
        result = 0
        # odd on n, even on m
        result += ((n-1)//2 + 1) * ((m-2)//2 + 1)
        # even on n, odd on m
        result += ((n-2)//2 + 1) * ((m-1)//2 + 1)
        return result
