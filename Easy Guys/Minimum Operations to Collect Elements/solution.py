class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collection = set()
        n = len(nums)
        while len(collection) < k and nums:
            num = nums.pop()
            if num <= k:
                collection.add(num)
        return n - len(nums)
            
