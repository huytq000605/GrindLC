class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        n = len(nums)
        for bit in range(31, -1, -1):
            # target prefix based on ongoing max_xor (set `bit`)
            target = (max_xor >> bit) | 1
            prefixes = set()
            # get prefix of all nums
            for num in nums:
                pref = num >> bit
                prefixes.add(pref)
            for pref in prefixes:
                if pref ^ target in prefixes:
                    max_xor |= (1 << bit)
                    break
        return max_xor
