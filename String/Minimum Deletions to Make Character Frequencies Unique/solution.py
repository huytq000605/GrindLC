class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        frequencies = sorted(counter.values(), reverse = True)
        result = 0
        next_num = frequencies[0]
        for freq in frequencies:
            next_num = min(next_num, freq)
            result += freq - next_num
            if next_num > 0:
                next_num -= 1
        return result