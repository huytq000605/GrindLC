# Binary Lifting

## Query KthAncestor for any node in a tree (1483 LC)

- Build parents for all node => O(kn) space
- Each time go find, O(kn) time
  
- The best way to do this is using Binary Lifting:
1. We choose max step to go (assume we have  max nodes = 5*10^4) => Max step = 15 (Each node has max 15 parents)
2. For each step, we find 2^i parent of each node
3. For every query, we do it in O(logn) time

``` python
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
```