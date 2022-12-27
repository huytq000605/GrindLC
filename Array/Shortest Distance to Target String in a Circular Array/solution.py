class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        result = n+1
        for i, word in enumerate(words):
            if word == target:
                result = min(result, abs(i - startIndex), n - abs(i - startIndex))
        if result == n+1:
            return -1
        return result
