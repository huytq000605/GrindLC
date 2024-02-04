class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        result = 0
        idx = 2
        times = 1
        for c, freq in sorted(counter.items(), key = lambda e: -e[1]):
            result += times * freq
            idx += 1
            if idx == 10:
                idx = 2
                times += 1
        return result
