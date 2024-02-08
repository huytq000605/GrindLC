class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        m = len(s) // 2
        s1 = s[:m]
        s2 = s[m:][::-1]
        diffs = []
        for i in range(m):
            if s1[i] != s2[i]:
                diffs.append(i)
        if not diffs: return [True for _ in range(len(queries))]        

        def cover_all_diffs(a, b, c, d):
            if c < a:
                a, b, c, d = c, d, a, b
            if a > diffs[0] or max(b, d) < diffs[-1]: return False
            need_cover_from = bisect.bisect_right(diffs, b)
            if need_cover_from == len(diffs): return True
            return c <= diffs[need_cover_from]

        counter1, counter2 = [[0 for _ in range(26)]], [[0 for _ in range(26)]]
        offset = ord('a')
        for i in range(m):
            c1, c2 = ord(s1[i]) - offset, ord(s2[i]) - offset
            counter1.append([*counter1[-1]])
            counter2.append([*counter2[-1]])
            counter1[-1][c1] += 1
            counter2[-1][c2] += 1

        def same_set_chars(a, b):
            if a > b: return True
            count1 = [counter1[b+1][c] - counter1[a][c] for c in range(26)]
            count2 = [counter2[b+1][c] - counter2[a][c] for c in range(26)]
            return all([count1[c] == count2[c] for c in range(26)])

        def same_intersect_set_chars(a, b, c, d):
            # non overlapping
            if max(a, c) > min(b, d):
                return same_set_chars(a, b) and same_set_chars(c, d)
            c1, c2 = counter1, counter2
            if c < a:
                a, b, c, d = c, d, a, b
                c1, c2 = c2, c1
            # [a:b] cover
            if b >= d:
                return same_set_chars(a, b)
            # [c:d] cover all
            if c == a:
                return same_set_chars(c, d)
            # check full ranges
            if not same_set_chars(a, d):
                return False
            # a .. c .. b .. d
            # overlapping range [c..b]
            # non overlapping ranges [a..c-1] and [b+1..d]
            for i in range(26):
                # s1[a..b] should cover s2[a..c-1]
                if c1[b+1][i] - c1[a][i] < c2[c][i] - c2[a][i]:
                    return False
                # s2[c..d] should cover s1[b+1..d]
                if c2[d+1][i] - c2[c][i] < c1[d+1][i] - c1[b+1][i]:
                    return False
            return True


        result = []
        for a, b, c, d in queries:
            c, d = m - 1 - (d - m), m - 1 - (c - m)
            if not cover_all_diffs(a, b, c, d):
                result.append(False)
                continue
            # overlapping
            
            result.append(same_intersect_set_chars(a, b, c, d))
            
        return result
