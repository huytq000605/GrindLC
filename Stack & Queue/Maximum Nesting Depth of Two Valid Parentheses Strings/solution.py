class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        result = [0 for _ in range(len(seq))]
        s1, s2 = 0, 0
        for i in range(len(seq)):
            c = seq[i]
            if c == '(':
                if s1 <= s2:
                    s1 += 1
                else:
                    s2 += 1
                    result[i] = 1
            else:
                if s1 >= s2:
                    s1 -= 1
                else:
                    s2 -= 1
                    result[i] = 1
        return result
