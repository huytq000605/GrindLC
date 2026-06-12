# Segment Tree

**Idea:** A segment tree supports efficient range queries (sum, max, etc.) in `O(log n)`. Each node stores aggregated values for a segment, so a query touches only `O(log n)` nodes instead of scanning the whole range.

## Notes
- There are two common implementations in DS & Algo: an **array** implementation and a **tree** (pointer/node) implementation.
- Building the tree with the recursive `build` is `O(n)`; building by inserting/updating the `n` elements one at a time is `O(n log n)`.
- Each node can store **multiple values** in its properties (e.g. sum and sum of squares, or prefix/suffix/max sums) to solve richer problems.

## Template: Range Add with Lazy Propagation (sum and sum of squares)

This variant supports range updates (add `val` to a range) using lazy propagation, while maintaining both the sum and the sum of squares of each segment.

The key algebra for updating the sum of squares when adding `x` to every element:

- `(a+1)**2 = a**2 + 2*a + 1` (considering `gap = 2`)
- `(a+1)**2 + (b+1)**2 = a**2 + b**2 + 2*(a+b) + 2`
- `(a+x)**2 + (b+x)**2 = a**2 + b**2 + 2*x*(a + b) + 2 * x**2`

```python
MOD = 10**9 + 7

class SegmentTree:
    def __init__(self, n):
        self.sum = [0 for _ in range(4*n)]
        self.sum_sq = [0 for _ in range(4*n)]
        self.lazy = [0 for _ in range(4*n)]
        self.n = n

    def __update_lazy(self, left, right, i):
        if left != right:
            self.lazy[i*2+1] += self.lazy[i]
            self.lazy[i*2+2] += self.lazy[i]
        gap = right - left + 1
        # 1. (a+1)**2 = a**2 + 2*a + 1
        # considering gap = 2
        # 2. (a+1)**2 + (b+1)**2 = a**2+ b**2 + 2*(a+b) + 2
        # 3. (a+x)**2 + (b+x)**2 = a**2 + b**2 + 2*x*(a + b) + 2 * x**2
        new_sum = self.sum[i] + self.lazy[i] * gap
        new_sum_sq = self.sum_sq[i] + 2 * self.lazy[i] * self.sum[i] + (self.lazy[i]**2) * gap
        self.sum[i] = new_sum % MOD
        self.sum_sq[i] = new_sum_sq % MOD
        self.lazy[i] = 0
    
    
    def add(self, start, end, val, left = 0, right = -1, i = 0):
        if right == -1: right = self.n - 1
        if self.lazy[i]:
            self.__update_lazy(left, right, i)

        if start > right or end < left:
            return
        
        if start <= left and end >= right:
            self.lazy[i] += val
            self.__update_lazy(left, right, i)
            return

        mid = left + (right - left) // 2
        self.add(start, end, val, left, mid, i*2+1)
        self.add(start, end, val, mid + 1, right, i*2+2)
        
        self.sum[i] = (self.sum[i*2+1] + self.sum[i*2+2]) % MOD
        self.sum_sq[i] = (self.sum_sq[i*2+1] + self.sum_sq[i*2+2]) % MOD
```

## Template: Maximum Subarray Sum (prefix / suffix / total / max)

Each node stores four values so segments merge into the maximum subarray sum: `total_sum`, `prefix_sum`, `suffix_sum`, and `max_sum`. The merge combines a left child's suffix with a right child's prefix to span the boundary.

```cpp
class SegmentTree {
struct Node {
    long long total_sum, prefix_sum, suffix_sum, max_sum;
};
vector<Node> tree;
int n;

public:
    SegmentTree(int _n): n(_n) {
        tree.resize(4 * n);
    }

    Node query(int start, int end, int l = 0, int r = -1, int i = 0) {
        if(r == -1) r = n-1;
        if(start <= l && end >= r) return tree[i];
        if(start > r || end < l) return {0, LLONG_MIN, LLONG_MIN, LLONG_MIN};
        int mid = l + (r - l) / 2;
        Node left = query(start, end, l, mid, i*2+1);
        Node right = query(start, end, mid+1, r, i*2+2);
        Node result;
        result.prefix_sum = max(left.total_sum + right.prefix_sum, left.prefix_sum);
        result.suffix_sum = max(left.suffix_sum + right.total_sum, right.suffix_sum);
        result.total_sum = left.total_sum + right.total_sum;
        result.max_sum = max({left.max_sum, right.max_sum, left.suffix_sum + right.prefix_sum});
        return result;
    }

    void update(int start, int end, long long val, int l = 0, int r = -1, int i = 0) {
        if(r == -1) r = n-1;
        if(start <= l && end >= r) {
            tree[i] = {val, val, val, val};
            return;
        }
        if(start > r || end < l) return;
        int mid = l + (r - l) / 2;
        update(start, end, val, l, mid, i*2+1);
        update(start, end, val, mid+1, r, i*2+2);
        Node left = tree[i*2+1];
        Node right = tree[i*2+2];
        tree[i].prefix_sum = max(left.total_sum + right.prefix_sum, left.prefix_sum);
        tree[i].suffix_sum = max(left.suffix_sum + right.total_sum, right.suffix_sum);
        tree[i].total_sum = left.total_sum + right.total_sum;
        tree[i].max_sum = max({left.max_sum, right.max_sum, left.suffix_sum + right.prefix_sum});
    }

    Node build(vector<int> &nums, int l = 0, int r = -1, int i = 0) {
        if(r == -1) r = n-1;
        if(l == r) {
            tree[i] = {nums[l], nums[l], nums[l], nums[l]};
            return tree[i];
        } else {
            int mid = l + (r - l) / 2;
            Node left = build(nums, l, mid, i*2+1);
            Node right = build(nums, mid+1, r, i*2+2);
            tree[i].prefix_sum = max(left.total_sum + right.prefix_sum, left.prefix_sum);
            tree[i].suffix_sum = max(left.suffix_sum + right.total_sum, right.suffix_sum);
            tree[i].total_sum = left.total_sum + right.total_sum;
            tree[i].max_sum = max({left.max_sum, right.max_sum, left.suffix_sum + right.prefix_sum});
            return tree[i];
        }
    }
};
```

## Complexity
- **Time:** `O(log n)` per query/update; `O(n)` to build with `build` (recursive bottom-up over `n` leaves).
- **Space:** `O(n)` for the tree array (sized `4*n`).
