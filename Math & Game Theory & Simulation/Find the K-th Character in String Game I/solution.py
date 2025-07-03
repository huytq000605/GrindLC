class Solution:
    def kthCharacter(self, k: int) -> str:
        t = ceil(log(k) / log(2))
        i = k-1
        n = 1 << t
        shift = 0
        while n > 1:
            n >>= 1
            if i >= n:
                i -= n
                shift += 1
        shift %= 26
        return chr(ord('a') + shift)
