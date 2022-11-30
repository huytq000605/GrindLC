class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        counterFreq = Counter(counter.values())
        for freq_freq in counterFreq.values():
            if freq_freq > 1:
                return False
        return True
