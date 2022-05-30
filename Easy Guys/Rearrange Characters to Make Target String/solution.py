class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter = Counter(s)
        count_target = Counter(target)
        result = math.inf
        for letter, freq in count_target.items():
            result = min(result, counter[letter] // freq)
        return result