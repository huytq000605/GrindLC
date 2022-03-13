class Solution:
    def distinctSubseqII(self, s: str) -> int:
        end_with = Counter()
        MOD = 10**9 + 7
        for letter in s:
            subsequences = 0
            for end_letter in end_with.keys():
                subsequences += end_with[end_letter]
            end_with[letter] = subsequences + 1
            end_with[letter] %= MOD
        return sum(end_with.values()) % MOD
