class Solution:
    def relocateMarbles(self, nums: List[int], f: List[int], t: List[int]) -> List[int]:
        pos = set()
        for num in nums:
            pos.add(num)
        
        n = len(f)
        for i in range(n):
            pos.remove(f[i])
            pos.add(t[i])
        
        return sorted(pos)
