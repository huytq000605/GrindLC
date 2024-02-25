class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        result = 0
        
        lps = [0 for _ in range(m)]
        j = 0
        for i in range(1, m):
            while j and pattern[i] != pattern[j]:
                j = lps[j-1]
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
        
        def match(diff, p):
            if p == 0 and diff != 0:
                return False
            if p != 0 and p * diff <= 0:
                return False
            return True
        
        j = 0
        for i in range(1, n):
            while j and not match(nums[i] - nums[i-1], pattern[j]):
                j = lps[j-1]
            if match(nums[i] - nums[i-1], pattern[j]):
                if j == len(lps) - 1:
                    result += 1
                    j = lps[j]
                else:
                    j += 1

        return result
