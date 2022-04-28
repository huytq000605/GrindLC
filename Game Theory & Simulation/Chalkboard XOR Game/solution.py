class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor = 0
        for num in nums:
            xor ^= num
        if xor == 0:
            return True
        n = len(nums)
        # The only way to make opponent lose next turn is let them have odd amount of same numbers
        # So we have 2 different situations before that
        # 1. All the numbers are the same => The opponent wins before that turn
        # 2. There are at least 2 values => The player just need to pick the number dont make them lose
        if n % 2 == 0:
            return True
        else:
            return False