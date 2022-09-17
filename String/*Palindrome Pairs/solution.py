class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        idxs = {w:i for i, w in enumerate(words)}
        
        def is_palindrome(word):
            return word == word[::-1]
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                first, second = word[:j], word[j:]
                
                if is_palindrome(first):
                    reverse_second = second[::-1]
                    if reverse_second in idxs and idxs[reverse_second] != i:
                        result.append((idxs[reverse_second], i))
                        
                if is_palindrome(second) and second != "":
                    reverse_first = first[::-1]
                    if reverse_first in idxs and idxs[reverse_first] != i:
                        result.append((i, idxs[reverse_first]))
        return result
                    
            
            
