class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        z = nums.index(0)  

        # we shift left, so shift right to get corresponding pos
        def is_valid(shift, reverse):
            if reverse:
                for i in range(n):
                    if nums[(i+shift)%n] != n-1-i:
                        return False
            else:
                for i in range(n):
                    if nums[(i+shift)%n] != i:
                        return False
            return True
        # make the nums become increasing list, either shift left z, or reverse then shift left (n-z) times then reverse 
        inc = min(z, (n-z)+2) if is_valid(z, False) else math.inf
        # make the nums become decreasing list, either shift left z+1 times then reverse, or reverse then n-1-z times
        dec = min(z+2, (n-1-z)+1) if is_valid(z+1, True) else math.inf
        result = min(inc, dec)
        if result == math.inf: return -1
        return result
