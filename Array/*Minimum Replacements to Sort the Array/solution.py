class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = nums[-1]
        result = 0
        for i in range(n-2, -1, -1):
            # How many partitions these operations will make
            k = math.ceil(nums[i] / max_num)
            # Partitions = Operations - 1
            result += k - 1
            # Find min partition
            max_num = nums[i] // k
        return result
