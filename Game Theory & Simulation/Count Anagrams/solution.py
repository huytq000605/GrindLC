class Solution:
    def countAnagrams(self, s: str) -> int:
        s = s.split(" ")
        MOD = 10**9 + 7
        result = 1
        for word in s:
            n = len(word)
            counter = Counter(word)
            for freq in counter.values():
                result *= math.comb(n, freq)
                n -= freq
                result %= MOD
        return result
