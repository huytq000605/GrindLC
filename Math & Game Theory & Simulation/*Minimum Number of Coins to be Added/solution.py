class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        coin = 0
        obtain_max = 0
        result = 0
        while obtain_max < target:
            if coin < len(coins) and coins[coin] <= obtain_max + 1:
                obtain_max += coins[coin]
                coin += 1
            else:
                obtain_max += obtain_max + 1
                result += 1
        return result
