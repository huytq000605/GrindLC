class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # For each letter, count how many times does it contribute to the result
        # => Count how many times it appears in a substring as a unique character
        n = len(s)
        result = 0
        last_2_position = [(-1, -1) for i in range(26)]
        for i, l in enumerate(s):
            char_code = ord(l) - ord('A')
            prev_last, last = last_2_position[char_code]
            result += ((last - 1) - (prev_last + 1) + 1 + 1) * ( (i-1) - (last+1) + 1 + 1)
            last_2_position[char_code] = (last, i)
        for i in range(26):
            prev_last, last = last_2_position[i]
            result += ((last - 1) - (prev_last + 1) + 1 + 1) * ( (n-1) - (last+1) + 1 + 1)
        return result