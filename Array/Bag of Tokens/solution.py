class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        result = 0
        tokens.sort()
        j = len(tokens) - 1
        for i, token in enumerate(tokens):
            while power < token and score and j > i:
                score -= 1
                power += tokens[j]
                j -= 1
            if power >= token:
                power -= token
                score += 1
                result = max(result, score)
            else:
                break
        return result
            
