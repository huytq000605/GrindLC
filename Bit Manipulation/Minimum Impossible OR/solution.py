class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        # if we cannot build a num
        # num must be pow of 2
        # prove:
        # if num is not pow of 2, for example: num = 0b1101
        # So that means we dont have 0b1000 or 0b0100 or 0b0001 that are contributed
        have = set(nums)
        for i in range(31):
            target = 1 << i
            if target not in have:
                return target
        return -1
