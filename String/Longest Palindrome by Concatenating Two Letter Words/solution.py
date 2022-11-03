class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        result = 0
        odd_palindrome = 0
        counter = Counter(words)
        for word, freq in counter.items():
            reverse = word[::-1]
            if word == reverse:
                result += len(word) * (freq // 2) * 2
                odd_palindrome = max(odd_palindrome, len(word) * (freq % 2))
            elif reverse in counter:
                result += min(freq, counter[reverse]) * len(word) * 2
                counter[word] = 0        
        return result + odd_palindrome
