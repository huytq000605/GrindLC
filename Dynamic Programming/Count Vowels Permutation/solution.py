class Solution:
    def countVowelPermutation(self, n: int) -> int:
        can_follow = {
            'a': 'e',
            'e': 'ai',
            'i': 'aeou',
            'o': 'ui',
            'u': 'a',
            ' ': 'ueoai'
        }
        MOD = 10**9 + 7
        @cache
        def count(i, prev):
            if i >= n:
                return 1
            result = 0
            for letter in can_follow[prev]:
                result += count(i + 1, letter)
            return result % MOD
        return count(0, ' ')
