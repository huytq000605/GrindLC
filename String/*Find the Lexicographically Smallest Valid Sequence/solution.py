class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        # can_match[i] = j means word1[i:] can match word2[j:]
        can_match = [0 for _ in range(len(word1) + 1)]
        j = len(word2) - 1
        for i in range(len(word1) - 1, -1, -1):
            if word1[i] == word2[j]:
                j -= 1
                if j == -1: break
            can_match[i] = j + 1
        change = True
        result = []
        j = 0
        for i in range(len(word1)):
            if (word1[i] == word2[j]) or (change and can_match[i+1] <= j+1):
                result.append(i)   
                if change: change = word1[i] == word2[j]
                j += 1
                if j == len(word2): break
        if j != len(word2): return []
        return result

        
