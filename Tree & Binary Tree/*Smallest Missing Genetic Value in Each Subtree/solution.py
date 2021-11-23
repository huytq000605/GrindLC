class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        childs = [[] for i in range(n)]
        for i in range(n):
            if parents[i] == -1: continue
            childs[parents[i]].append(i)
        
        seen = set()
        current = 1
        
        idxOne = -1
        for i in range(n):
            if nums[i] == 1:
                idxOne = i
                break
        if idxOne == -1:
            return result
        
        
        def dfs(node):
            nonlocal current
            seen.add(nums[node])
            while current in seen:
                current += 1
            for nextNode in childs[node]:
                if nums[nextNode] not in seen:
                    dfs(nextNode)
        
        node = idxOne
        while node != -1:
            dfs(node)
            result[node] = current
            node = parents[node]
        return result
        