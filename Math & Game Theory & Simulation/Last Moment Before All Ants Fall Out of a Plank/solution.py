class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        result = 0
        # when ant A meets and B at X
        # now ant A turns into ant B, and ant B turns into ant A an keep walking
        # so can assume that the collision doesnt affect anything
        for l in left:
            result = max(result, l)
        for r in right:
            result = max(result, n-r)
        return result
