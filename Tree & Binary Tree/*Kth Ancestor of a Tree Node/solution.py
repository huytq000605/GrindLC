
class TreeAncestor:
    def __init__(self, n: int, A: List[int]):
        self.step = 15
        parents = [A]
        for i in range(self.step):
            B = [-1 for i in range(n)]
            for j in range(n):
                if A[j] != -1:
                    B[j] = A[A[j]]
            
            A = B
            parents.append(B)
        self.parents = parents

    def getKthAncestor(self, node: int, k: int) -> int:
        step = self.step
        
        while k > 0 and node > -1:
            if k >= (1 << step):
                k -= (1<<step)
                node = self.parents[step][node]
            else:
                step -= 1
        return node
                
                
            


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)