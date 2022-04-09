class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        perfect = set()
        i = 0
        while i * i <= 2 * 10**9:
            perfect.add(i * i)
            i += 1
        result = 0
        
        def permutations(i):
            nonlocal result
            if i >= len(nums):
                result += 1
                return
            seen = set()
            for j in range(i, len(nums)):
                if nums[j] in seen:
                    continue
                seen.add(nums[j])
                if i > 0 and (nums[i-1] + nums[j]) not in perfect:
                    continue
                nums[j], nums[i] = nums[i], nums[j]
                permutations(i + 1)
                nums[j], nums[i] = nums[i], nums[j]

        permutations(0)
        return result