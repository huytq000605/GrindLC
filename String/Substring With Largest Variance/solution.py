class Solution:
    def largestVariance(self, s: str) -> int:
        result = 0
        counter = Counter(s)
        for c1 in string.ascii_lowercase:
            for c2 in string.ascii_lowercase:
                if c1 == c2 or counter[c1] == 0 or counter[c2] == 0:
                    continue
                count_c1, count_c2 = 0, 0
                remain_c2 = counter[c2]
                for c in s:
                    if c == c1:
                        count_c1 += 1
                    if c == c2:
                        count_c2 += 1
                        remain_c2 -= 1                 
                    # need at least one c2
                    if count_c1 - count_c2 < 0 and remain_c2:
                        count_c1, count_c2 = 0, 0
                    if count_c2 > 0:
                        result = max(result, count_c1 - count_c2)
        return result
