class BreakOut(Exception):
    pass

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        max_mask = 1 << n
        result = 0
        for mask in range(max_mask):
            truth = set()
            for i in range(n):
                if (mask >> i) & 1 == 1:
                    truth.add(i)
            try:
                for person in truth:
                    for i in range(n):
                        if i not in truth and statements[person][i] == 1:
                            raise BreakOut
                        if i in truth and statements[person][i] == 0:
                            raise BreakOut
                result = max(result, len(truth))
            except BreakOut:
                continue
        return result