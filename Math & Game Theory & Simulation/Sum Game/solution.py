class Solution:
    def sumGame(self, num: str) -> bool:
        left, right = 0, 0
        diff = 0
        n = len(num)
        for i in range(n//2):
            if num[i] != '?':
                diff += int(num[i])
            else:
                left += 1
            if num[n-1-i] != '?':
                diff -= int(num[n-1-i])
            else:
                right += 1
        d = abs(left - right)
        a = b = d // 2
        if d & 1: a += 1
        if left == right and diff == 0: return False
        if left > right and 9 * a <= -diff <= 9 * b: return False
        if left < right and 9 * a <= diff <= 9 * b: return False
        return True
