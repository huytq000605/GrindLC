
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.step = 15
        A = dict(enumerate(parent))
        parents = [A]
        for i in range(self.step):
            B = dict()
            for j in A.keys():
                if A[j] in A:
                    B[j] = A[A[j]]
            
            A = B
            parents.append(B)
        self.parents = parents

    def getKthAncestor(self, node: int, k: int) -> int:
        step = self.step
        
        while k > 0 and node > -1:
            if k >= (1 << step):
                k -= (1<<step)
                node = self.parents[step].get(node, -1)
            else:
                step -= 1
        return node
                
                
            
# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)