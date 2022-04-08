class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        skill_to_idx = dict()
        for idx, skill in enumerate(req_skills):
            skill_to_idx[skill] = idx
        
        @cache
        def dfs(i, mask):
            if i >= len(people):
                if mask == (1<<n) - 1:
                    return 0
                return len(people)
            else:
                size = dfs(i + 1, mask)
                for skill in people[i]:
                    idx = skill_to_idx[skill]
                    mask |= (1<<idx)
                size = min(size, dfs(i+1, mask) + 1)
                return size
            
        smallest_size = dfs(0, 0)
        result = []
        mask = 0
        
        for i, skills in enumerate(people):
            if len(result) + dfs(i + 1, mask) != smallest_size:
                for skill in skills:
                    mask |= (1 << skill_to_idx[skill])
                result.append(i)
        
        return result