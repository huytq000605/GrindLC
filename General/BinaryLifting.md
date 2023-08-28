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

##  Maximize Value of Function in a Ball Passing Game (LC 2836)
- Because each node has and only has one father, so this problem is actually the continuous jumping on the only path. Immediately thinks of the binary lifting.
- Binary lifting is suitable for problems like "father's father is the second-order father".
- For this problem, jump 2 steps equals to jump 1 step then jump 1 step; jump 4 steps means jump 2 steps then jumps 2 steps...
- The most commonly used implementation for the binary lifting is to maintain a jump table.
  - In the table dp, dp[u][i] means the jump 2^i step from u 
  - This table can be calculated level-by-level: jumps 2^i times equal to jumps 2^(i-1) and jumps 2^(i-1)
  - For position: pos[u][i]= pos[pos[u][i-1][i-1]
  - For profit: profit[u][i]= profit[u][i-1] + profit[pos[u][i-1]][i-1] (It may be changed by the meaning of profit).
- After we get the table, how to use it?
  - Obviously, kkk can be composed by some powers of 2 (that is, the binary representation of kkk).
  - Therefore, by enumerating the binary representation of kkk, the profit of kkk steps can be obtained by summing the profit of 2^i steps.
