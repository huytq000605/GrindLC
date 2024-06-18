class SparseVector:
    def __init__(self, nums: List[int]):
        self.vs = [(i, v) for i, v in enumerate(nums) if v > 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        vs1, vs2 = self.vs, vec.vs
        i, j = 0, 0
        result = 0
        while i < len(vs1) and j < len(vs2):
            if vs1[i][0] == vs2[j][0]:
                result += vs1[i][1] * vs2[j][1]
                i += 1
                j += 1
            elif vs1[i][0] < vs2[j][0]:
                i += 1
            else:
                j += 1
        return result
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
