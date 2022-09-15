class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i, j = 0, len(tokens) - 1
        result = 0
        cur = 0
        while i <= j:
            if power >= tokens[i]:
                cur += 1
                power -= tokens[i]
                i += 1     
            elif cur > 0:
                cur -= 1
                power += tokens[j]
                j -= 1
            else:
                break
            result = max(result, cur)
        return result
