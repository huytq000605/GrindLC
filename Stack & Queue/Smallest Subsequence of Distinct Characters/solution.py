class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter()
        for l in s:
            freq[l] += 1
        result = []
        seen = set()
        for l in s:
            freq[l] -= 1
            while len(result) > 0 and l not in seen and result[-1] > l and freq[result[-1]] > 0:
                seen.remove(result.pop())
            if l not in seen:
                result.append(l)
                seen.add(l)
        return "".join(result)