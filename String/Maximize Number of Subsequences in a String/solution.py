class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a, b = pattern[0], pattern[1]
        count_a, count_b = 0, 0
        result = 0
        
        for l in text:
            # check b first for case a == b
            if l == b:
                count_b += 1
                result += count_a
            if l == a:
                count_a += 1
        return result + max(count_a, count_b)