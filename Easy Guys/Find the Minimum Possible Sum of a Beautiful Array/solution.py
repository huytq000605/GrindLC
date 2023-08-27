class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        s = 0
        have = set()
        num = 1
        while num < n + 1:
            if target - num not in have:
                have.add(num)
                s += num
            else:
                n += 1
            num += 1
        return s
                
