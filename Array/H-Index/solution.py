class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counter = [0 for i in range(1001)]
        for c in citations:
            counter[c] += 1
        n = len(citations)
        result = 0
        seen = 0
        for i in range(1001):
            if n - seen >= i:
                result = i
            seen += counter[i]
        return result
