class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []
        freq = Counter(s)
        in_result = set()
        for l in s:
            while l not in in_result and len(result) and result[-1] > l and freq[result[-1]] > 0:
                in_result.remove(result.pop())
            freq[l] -= 1
            if l not in in_result:
                in_result.add(l)
                result.append(l)
        return "".join(result)