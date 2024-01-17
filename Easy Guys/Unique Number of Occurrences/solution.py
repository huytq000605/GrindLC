class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        freq_counter = Counter(counter.values())
        for freq_freq in freq_counter.values():
            if freq_freq > 1:
                return False
        return True
