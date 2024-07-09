class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = 0
        for c in counter.values():
            if c == 1: return -1
            if c % 2 == 1:
                c -= 3
                result += 1
            twos = c // 2
            result += twos // 3 * 2 + (twos % 3)
            
        return result
