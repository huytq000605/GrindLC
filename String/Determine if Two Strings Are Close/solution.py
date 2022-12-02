class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1, counter2 = Counter(word1), Counter(word2)
        if len(counter1) != len(counter2):
            return False
        for c in counter1.keys():
            if c not in counter2:
                return False
            
        counter_counter1 = Counter(counter1.values())
        for c, f in counter2.items():
            if counter_counter1[f] <= 0:
                return False
            counter_counter1[f] -= 1
        return True
