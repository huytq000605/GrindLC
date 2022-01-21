class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        n = len(arr)
        same_value = defaultdict(list)
        
        for i in range(n):
            same_value[arr[i]].append(i)
        
        seen = set()
        queue = deque([(0, 0)])
        seen.add(0)
        while queue:
            current_node, step = queue.popleft()
            if current_node < n-1 and current_node + 1 not in seen:
                if current_node + 1 == n-1:
                    return step + 1
                seen.add(current_node + 1)
                queue.append((current_node + 1, step + 1))
                
            if current_node > 0 and current_node -1 not in seen:
                seen.add(current_node - 1)
                queue.append((current_node - 1, step + 1))
                
            for next_node in same_value[arr[current_node]]:
                if next_node in seen:
                    continue
                if next_node == n-1:
                    return step + 1
                seen.add(next_node)
                queue.append((next_node, step + 1))
            
            same_value[arr[current_node]] = []
        
        return -1