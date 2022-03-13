class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idxs = []
        for i, num in enumerate(nums):
            if num == key:
                idxs.append(i)
        result = set()
        for j in range(len(nums)):
            for i in idxs:
                if abs(j - i) <= k:
                    result.add(j)
        return result