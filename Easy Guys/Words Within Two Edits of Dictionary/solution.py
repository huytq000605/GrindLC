class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for query in queries:
            valid = False
            for word in dictionary:
                if len(query) != len(word):
                    continue
                n = len(query)
                diff = 0
                for i in range(n):
                    if query[i] != word[i]:
                        diff += 1
                if diff <= 2:
                    valid = True
                    break
            if valid:
                result.append(query)
        return result
