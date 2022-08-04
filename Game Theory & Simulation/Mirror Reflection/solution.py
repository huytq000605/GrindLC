class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        k = 1
        while q * k % p:
            k += 1
        if k % 2 == 0:
            return 2
        wall_times = q * k // p
        if wall_times % 2 == 0:
            return 0
        else:
            return 1
