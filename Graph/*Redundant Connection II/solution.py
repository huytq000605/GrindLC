class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        wrong1, wrong2 = [], []
        n = len(edges)
        parents = [0 for i in range(n + 1)]
        
        # Loop through all edges
        # If there are node with 2 parents 
        # => Assign the first with wrong1 and the later with wrong2
        for u, v in edges:
            if parents[v] == 0:
                parents[v] = u
            else:
                wrong1 = [parents[v], v]
                wrong2 = [u, v]
        
        # Unionfind function
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        # Set parents (UF)
        parents = [i for i in range(n + 1)]
        
        
        for u, v in edges:
            # Ignore edge wrong2 if have
            if len(wrong2) > 0 and u == wrong2[0] and v == wrong2[1]:
                continue
            u_p = find(u)
            
            # If have a circle
            if u_p == v:
                # If we have wrong1 => wrong1 is the redundant
                # Because we're ignoring the wrong2 so wrong1 is the edge that make the circle
                # If no wrong1 and wrong2 then return this edge
                if len(wrong1) == 0:
                    return [u, v]
                else:
                    return wrong1
            parents[v] = u_p
            
        return wrong2