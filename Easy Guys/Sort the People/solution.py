class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        return map(lambda e: e[1], sorted([(-heights[i], names[i]) for i in range(n)]))
