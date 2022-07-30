class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq = [0 for i in range(26)]
        for word in words2:
            current = [0 for i in range(26)]
            for c in word:
                idx = ord(c) - ord('a')
                current[idx] += 1
                freq[idx] = max(freq[idx], current[idx])

        def is_universal(word):
            nonlocal freq
            current = [0 for i in range(26)]
            for c in word: 
                current[ord(c) - ord('a')] += 1
            for i in range(26):
                if freq[i] > current[i]:
                    return False
            return True

        result = []
        for word in words1:
            if is_universal(word):
                result.append(word)

        return result
