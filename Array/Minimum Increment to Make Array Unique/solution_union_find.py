class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        parent = {}
        def find(u):
            if u not in parent: parent[u] = u
            else: parent[u] = find(parent.get(u+1, u+1))
            return parent[u]
        return sum([find(u) - u for u in nums])
