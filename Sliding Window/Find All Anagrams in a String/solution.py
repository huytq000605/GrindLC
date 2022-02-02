class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        current_letters = [0 for i in range(26)]
        target_letters = [0 for i in range(26)]
        result = []
        
        def idx_letter(l):
            return ord(l) - ord("a")
        
        def is_anagram():
            for i in range(26):
                if current_letters[i] != target_letters[i]:
                    return False
            return True
        
        for l in p:
            target_letters[idx_letter(l)] += 1
        
        for i in range(len(s)):
            if i >= k:
                current_letters[idx_letter(s[i - k])] -= 1
            current_letters[idx_letter(s[i])] += 1
            
            if i >= k-1 and is_anagram():
                result.append(i - k + 1)
        return result
