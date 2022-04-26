class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        two_nums = defaultdict(int)
        for a in nums:
            for b in nums:
                two_nums[a&b] += 1
        result = 0
        # Because of nums[i] < 2^16 => We have two_nums have maximum number of keys = 2^16
        # Time complexity: n * 2^16
        for c in nums:
            for d, freq in two_nums.items():
                if c & d == 0:
                    result += freq
        return result