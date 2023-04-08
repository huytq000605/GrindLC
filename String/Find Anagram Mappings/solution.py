class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idxs = defaultdict(list)
        for i, num in enumerate(nums2):
            idxs[num].append(i)
        result = [0 for _ in range(len(nums1))]
        for i, num in enumerate(nums1):
            result[i] = idxs[num].pop()
        return result
