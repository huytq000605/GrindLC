class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = "aeiou"

        def atMost(k):
            result = 0
            freq = {}
            start = 0
            for i in range(len(word)):
                if word[i] in vowels:
                    if word[i] not in freq: freq[word[i]] = 0
                    freq[word[i]] += 1
                else:
                    freq = {}
                    start = i + 1
            
                while len(freq) > k:
                    freq[word[start]] -= 1
                    if freq[word[start]] == 0:
                        del freq[word[start]]
                    start += 1
                result += i - start + 1
                
            return result

        return atMost(5) - atMost(4)