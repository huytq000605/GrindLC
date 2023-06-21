class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows = set()
        cols  = set()
        result = 0
        for query in reversed(queries):
            typei, indexi, vali = query
            if typei == 0 and indexi not in rows:
                result += vali * (n - len(cols))
                rows.add(indexi)
            if typei == 1 and indexi not in cols:
                result += vali * (n - len(rows))
                cols.add(indexi)
        return result
