class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for remove in counter.keys():
            value = -1
            valid = True
            for k, v in counter.items():
                if k == remove:
                    v -= 1
                if v == 0:
                    continue
                if value == -1:
                    value = v
                if value != v:
                    valid = False
                    break
            if valid:
                return True
        return False
            
