class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        prev = 0
        # assume considering i, j with i <= j
        # result += nums[j] ^ 2 * nums[i] * 2 ^ (j - i - 1)
        # So that means nums[j] contributed by
        # S(j) = nums[j]^3 + nums[j] ^ 2 * C(j)
        # C(j) = sum of (nums[i] * 2 ^ (j - i - 1)) for i < j
        # We could see that with every new j, C(j) = 2 * C(j-1) + nums[j]
        # Because number of groups for all previous one will be double
        # And plus with nums[j] is a group itself.
        result = 0
        for num in nums:
            result += num ** 3 + num ** 2 * prev
            result %= MOD
            prev = (prev * 2) + num
        return result
