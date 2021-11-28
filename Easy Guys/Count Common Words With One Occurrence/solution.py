class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        set1 = set()
        set2 = set()
        passed = set()
        for word in words1:
            if word in passed:
                continue
            if word in set1:
                set1.remove(word)
                passed.add(word)
                continue
            set1.add(word)
            
        for word in words2:
            if word in passed:
                continue
            if word in set2:
                set2.remove(word)
                passed.add(word)
                continue
            set2.add(word)
        
        return len(set1.intersection(set2))