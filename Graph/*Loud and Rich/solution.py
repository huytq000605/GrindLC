from typing import Dict, List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richerMap = {}
        for i in range(len(quiet)):
            richerMap[i] = []
        for rich in richer:
            richerMap[rich[1]].append(rich[0])
    
        result = [0] * len(quiet)
        seen = {}
        
        def dfs(currentPerson: int, seen: Dict) -> int:
            if seen.get(currentPerson) != None:
                return seen[currentPerson]
            result = currentPerson
            for richerPerson in richerMap[currentPerson]:
                if quiet[dfs(richerPerson, seen)] < quiet[result]:
                    result = dfs(richerPerson, seen)
            seen[currentPerson] = result
            return result
        
        for i in range(len(quiet)):
            result[i] = dfs(i, seen)
        return result
            