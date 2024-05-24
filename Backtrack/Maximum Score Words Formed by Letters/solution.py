class BreakOut(Exception):
    pass

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        m = len(letters)
        
        count_letter = [0 for i in range(26)]
        for l in letters:
            count_letter[ord(l) - ord("a")] += 1
        max_mask = 1 << n
        result = 0
        
        for mask in range(max_mask):
            try:
                current_score = 0
                current_letter = [0 for i in range(26)]
                for i in range(n):
                    if (mask >> i) & 1 == 1:
                        for l in words[i]:
                            letter_idx = ord(l) - ord("a")
                            current_letter[letter_idx] += 1
                            if current_letter[letter_idx] > count_letter[letter_idx]:
                                raise BreakOut
                            current_score += score[letter_idx]
                result = max(result, current_score)

            except BreakOut:
                continue
        return result
