class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        # Split the entire square into multiple sideLength squares
        # For example width = 5, height = 5, sideLength = 2
        # 0 1 | 0 1 | 0
        # 2 3 | 2 3 | 2
        # -------------
        # 0 1 | 0 1 | 0
        # 2 3 | 2 3 | 2
        # -------------
        # 0 1 | 0 1 | 0

        # We index the position in sideLength squares
        # Now we only need to include top `maxOnes` the indexs that appear the most

        pq = []
        for r in range(sideLength):
            for c in range(sideLength):
                vertical = (height - 1 - r) // sideLength + 1
                horizontal = (width - 1 - c ) // sideLength + 1
                heappush(pq, vertical * horizontal)
                if len(pq) > maxOnes:
                    heappop(pq)
        return sum(pq)

