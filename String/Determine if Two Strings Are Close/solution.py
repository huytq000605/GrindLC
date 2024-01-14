class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        counter = Counter(word1)
        counter2 = Counter(word2)
        for c in counter.keys():
            if c not in counter2: return False
        freq_counter = Counter(counter.values())
        for freq in counter2.values():
            freq_counter[freq] -= 1
            if freq_counter[freq] < 0:
                return False
        return True
