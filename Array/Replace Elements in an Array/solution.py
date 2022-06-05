class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        idxs = dict()
        for i, num in enumerate(nums):
            idxs[num] = i
            
        for u, v in operations:
            idx = idxs[u]
            nums[idx] = v
            idxs.pop(u)
            idxs[v] = idx
                
        return nums