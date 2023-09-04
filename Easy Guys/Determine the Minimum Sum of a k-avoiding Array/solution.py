class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        s = set()
        num = 1
        result = 0
        while len(s) < n:
            if k - num not in s:
                s.add(num)
                result += num
            num += 1
        return result
            
