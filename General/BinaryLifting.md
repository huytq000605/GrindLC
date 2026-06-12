# Binary Lifting

**Idea:** Precompute, for every node, where you land after jumping `2^i` steps. Any jump of `k` steps then decomposes into the binary representation of `k`, so each query runs in `O(log n)` instead of walking the path one step at a time. Binary lifting fits problems where "the father's father is the second-order father" — i.e. repeated jumps along a chain where each node has exactly one successor.

## Build the jump table

Maintain a table `dp` where `dp[u][i]` = the node reached after jumping `2^i` steps from `u`. Build it level by level, since jumping `2^i` steps equals jumping `2^(i-1)` then another `2^(i-1)`:

- Position: `pos[u][i] = pos[pos[u][i-1]][i-1]`
- Profit (if the problem accumulates a value): `profit[u][i] = profit[u][i-1] + profit[pos[u][i-1]][i-1]` (adjust to whatever "profit" means in the problem).

## Query the K-th ancestor (LC 1483)

Naive approaches:

- Build parents for all nodes => `O(kn)` space.
- Each lookup walks up step by step => `O(kn)` time.

Binary lifting does better:

1. Choose the max step. With up to `5 * 10^4` nodes, `max step = 15` (each node tracks up to 15 levels of ancestors).
2. For each step `i`, compute the `2^i`-th parent of every node.
3. Answer each query in `O(log n)` time.

```python
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

## Apply to Maximize Value of Function in a Ball Passing Game (LC 2836)

Each node has exactly one father, so the problem is really continuous jumping along a single path — a textbook fit for binary lifting.

- Jumping 2 steps = jump 1 then jump 1; jumping 4 steps = jump 2 then jump 2; and so on.
- Build the jump table as described above, tracking both position and accumulated profit.

Using the table:

- `k` can be composed from powers of 2 (its binary representation).
- So by enumerating the set bits of `k`, the profit over `k` steps is the sum of the profits of the corresponding `2^i` steps.

## Complexity

- **Time:** `O(n log n)` to build the table; `O(log n)` per query.
- **Space:** `O(n log n)` for the table.
