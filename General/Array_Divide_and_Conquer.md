# Array Divide and Conquer (Problems Similar to "Reverse Pairs")

## Idea

Many array problems have several known solutions (BST-based, BIT-based, Merge-sort-based). Here the focus is on the **general principles** behind these solutions and how they apply to a family of similar problems.

The fundamental idea is simple: **break the array down and solve the subproblems.**

Breaking an array down naturally points us to **subarrays**. To set up notation, assume the input array is `nums` with `n` elements. Let `nums[i, j]` denote the subarray from index `i` to index `j` (both inclusive), and let `T(i, j)` be the same problem applied to that subarray. (For example, for Reverse Pairs, `T(i, j)` is the total number of important reverse pairs in `nums[i, j]`.)

With this definition, the original problem is just `T(0, n - 1)`. The key question is how to construct the solution of the original problem from its subproblems — i.e., how to build **recurrence relations** for `T(i, j)`. Once we can solve `T(i, j)` from its subproblems, we can keep building up to larger subarrays until the whole array is spanned.

There are many possible recurrence relations; here we use the two most common ones:

1. **Sequential recurrence relation:** `T(i, j) = T(i, j - 1) + C`. Elements are processed one at a time, and `C` is the subproblem of processing the last element of `nums[i, j]`.

2. **Partition recurrence relation:** `T(i, j) = T(i, m) + T(m + 1, j) + C` where `m = (i + j) / 2`. The subarray `nums[i, j]` is split into two halves, and `C` is the subproblem of combining the two parts.

In both cases, the nature of subproblem `C` depends on the specific problem, and it determines the overall time complexity. So finding an **efficient algorithm for `C`** is usually crucial for good performance. Also watch for **overlapping subproblems**, in which case a dynamic programming (DP) approach is preferred.

Next we apply these two recurrence relations to "Reverse Pairs" and list some reference solutions.

## Sequential Recurrence Relation

Assume the input array is `nums` with `n` elements and `T(i, j)` is the number of important reverse pairs in `nums[i, j]`. For the sequential recurrence relation we can set `i = 0`, so the subarray always starts from the beginning:

```
T(0, j) = T(0, j - 1) + C
```

Here subproblem `C` becomes: *find the number of important reverse pairs whose first element comes from `nums[0, j - 1]` and whose second element is `nums[j]`.*

For a pair `(p, q)` to be an **important reverse pair**, it must satisfy two conditions:

1. `p < q` — the first element comes before the second;
2. `nums[p] > 2 * nums[q]` — the first element is greater than twice the second.

For subproblem `C`, the first condition holds automatically, so we only need the second one: search `nums[0, j - 1]` for all elements greater than `2 * nums[j]`.

The straightforward approach is a **linear scan** of the subarray, which runs in `O(j)`. Combined with the sequential recurrence relation, this gives the naive `O(n^2)` solution.

To speed up the search, the key observation is that the **order of elements does not matter** — we only want the count of important reverse pairs. So we can sort those elements and use **binary search** instead of a linear scan.

If the search space (the set of elements we search over) were *static* (unchanging from run to run), storing the elements in an array would be perfect for binary search. But that is not the case here: after processing the `j`-th element, we must add it to the search space so later elements can see it, which makes the search space **expand** as more elements are processed.

We therefore want a balance between **search** and **insertion**. This is where structures like a **binary search tree (BST)** or **binary indexed tree (BIT)** shine, offering relatively fast performance on both operations.

> Note: A plain BST has worst-case `O(n^2)`. Use a **self-balanced BST** to guarantee `O(n log n)`.

## Partition Recurrence Relation

```
T(0, n - 1) = T(0, m) + T(m + 1, n - 1) + C
```

Here subproblem `C` reads: *find the number of important reverse pairs whose first element comes from the left subarray `nums[0, m]` and whose second element comes from the right subarray `nums[m + 1, n - 1]`.*

Again the first of the two conditions holds automatically. For the second condition, the plain linear scan (applied for each element in the left or right subarray) once more leads to the naive `O(n^2)` solution.

Fortunately the same observation holds: the order of elements within the left or right subarray does not matter, so we can **sort** both subarrays. With both subarrays sorted, the number of important reverse pairs can be found in **linear time** using the **two-pointer technique** — one pointer over the left subarray, one over the right, each moving in a single direction thanks to the ordering.

The last question is which sorting algorithm to use. Since we partition the array into halves anyway, it is most natural to adapt this into a **Merge-sort**. A further advantage: the search above can be embedded **seamlessly into the merge step**.

## Summary

Many array problems can be solved by breaking the problem into **subproblems on subarrays** and linking the original solution to the subproblem solutions, via either the **sequential** or the **partition** recurrence relation. In both cases, it is crucial to identify subproblem `C` and find an efficient algorithm for it.

- If `C` involves **searching on a dynamic search space**, consider data structures with fast search and update on both ends (self-balanced BST, BIT, Segment tree, ...).
- If `C` of the **partition** recurrence involves **sorting**, Merge-sort is a good choice. The code is more elegant when the subproblem solution can be embedded into the merge process.
- If the subproblems `T(i, j)` **overlap**, cache the intermediate results for future lookup (DP).

## Related LeetCode Problems

- **315. Count of Smaller Numbers After Self**
- **327. Count of Range Sum**

**LeetCode 315:** With the sequential recurrence relation (`j` fixed), `C` is "find the number of already-visited elements smaller than the current element" — searching on a dynamic search space. With the partition recurrence relation, `C` is "for each element in the left half, find the number of elements in the right half smaller than it", which can be embedded into the merge process by noting that these are exactly the elements swapped to its left during merging.

**LeetCode 327:** With the sequential recurrence relation (`j` fixed) on the **prefix-sum array**, `C` is "find the number of already-visited elements within the given range" — again searching on a dynamic search space. With the partition recurrence relation, `C` is "for each element in the left half, find the number of elements in the right half within the given range", which can be embedded into the merge process using the two-pointer technique.
