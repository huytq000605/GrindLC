class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        words.sort(key = lambda w: len(w))
        counter = Counter()
        for word in words:
            for c in word:
                counter[c] += 1
        
        odd = 0
        even = 0
        for v in counter.values():
            if v & 1: 
                odd += 1
                v -= 1
            even += v

        result = 0
        for word in words:
            m = len(word)
            palindrome = True
            
            if m & 1:
                m -= 1
                if odd:
                    odd -= 1
                elif even: 
                    even -= 2
                    odd += 1
                else:
                    palindrome = False
                
            even -= m
            if even < 0:
                palindrome = False
                
            if not palindrome:
                break
            result += 1
        return result
