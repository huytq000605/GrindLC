class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        counter = Counter()
        n = len(word)
        for i in range(0, n, k):
            counter[word[i:i+k]] += 1
        return (n // k) - max(counter.values())
