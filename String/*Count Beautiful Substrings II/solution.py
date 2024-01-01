class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        # (l / 2) * (l / 2) % k == 0
        # l**2 % (4*k) == 0
        l = 1
        k *= 4 
        while l ** 2 % k != 0:
            l += 1
        diff = 0
        # seen[remain][diff] = 
        # number of subarray with length % l == remain and
        # number of vowels - number of consonants == diff
        seen = [Counter() for _ in range(l)]
        seen[0][0] = 1
        result = 0
        for i, c in enumerate(s):
            if c in "ueoai":
                diff += 1
            else:
                diff -= 1
            remain = (i+1) % l
            result += seen[remain][diff]
            seen[remain][diff] += 1
        return result

