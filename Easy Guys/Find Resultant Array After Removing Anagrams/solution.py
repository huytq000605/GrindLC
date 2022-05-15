class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        i = 0
        while i < len(words):
            while i + 1 < len(words) and sorted(words[i]) == sorted(words[i+1]):
                words.pop(i+1)
            i += 1
        return words