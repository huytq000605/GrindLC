class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        result = 0
        for i in range(left, right + 1):
            if words[i][0] in "ueoai" and words[i][-1] in "ueoai":
                result += 1
        return result
