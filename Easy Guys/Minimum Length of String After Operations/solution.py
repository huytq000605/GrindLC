class Solution:
    def minimumLength(self, s: str) -> int:
        counter = [0 for _ in range(26)]
        for c in s:
            k = ord(c) - ord('a')
            counter[k] += 1
            if counter[k] == 3: counter[k] -= 2
        return sum(counter)
