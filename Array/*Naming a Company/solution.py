class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d = [set() for i in range(26)]
        for idea in ideas:
            d[ord(idea[0]) - ord('a')].add(idea[1:])

        result = 0
        for i in range(26):
            for j in range(i+1, 26):
                set_a, set_b = d[i], d[j]
                same = set_a & set_b
                result += (len(set_a) - len(same)) * (len(set_b) - len(same))
        return result * 2