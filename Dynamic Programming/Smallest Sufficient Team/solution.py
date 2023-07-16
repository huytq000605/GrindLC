class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        mapping = dict()
        for i, skill in enumerate(req_skills):
            mapping[skill] = i
        masks = [0 for _ in range(len(people))]
        for i, p in enumerate(people):
            for skill in p:
               masks[i] |= (1 << mapping[skill])

        @cache
        def dfs(p, mask):
            if mask == (1 << len(mapping)) - 1:
                return 0
            if p >= len(people):
                return math.inf
            take = 1 + dfs(p+1, mask | masks[p])
            skip = dfs(p + 1, mask)
            return min(take, skip)

        result = []
        mask = 0
        for p in range(len(people)):
            if 1 + dfs(p+1, mask | masks[p]) <= dfs(p+1, mask):
                result.append(p)
                mask |= masks[p]
        return result


        
