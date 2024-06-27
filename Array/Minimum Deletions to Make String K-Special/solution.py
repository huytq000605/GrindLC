class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        result = math.inf
        for target in counter.values():
            res = 0
            for freq in counter.values():
                if freq < target: res += freq
                else: res += max(0, freq - target - k)
            result = min(result, res)
        return result
            
