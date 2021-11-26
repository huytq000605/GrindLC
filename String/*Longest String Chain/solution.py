class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        buckets = defaultdict(list)
        longest = dict()
        result = 1
        
        # Bucket Sort into word's length because 1 <= len(word) <= 16
        for word in words:
            length = len(word)
            buckets[length].append(word)
            longest[word] = 1
        
        
        # Go from highest len(word) to lowest, try to delete a letter from word to find longest path
        for length in sorted(buckets.keys(), reverse = True):
            for word in buckets[length]:
                for delPos in range(0, len(word)):
                    deletedWord = word[:delPos] + word[delPos + 1:]
                    if deletedWord in longest:
                        longest[deletedWord] = max(longest[deletedWord], longest[word] + 1)
                        result = max(result, longest[deletedWord])
        return result