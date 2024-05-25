class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]
            if (nums[i] ^ nums[i-1]) & 1 == 0:
                prefix[i] += 1
        result = []
        for a, b in queries:
            result.append(prefix[a] == prefix[b])
        return result
            
