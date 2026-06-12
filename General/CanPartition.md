# Partition Array into K Buckets

**Idea:** Deciding whether an array can be split into `k` partitions (buckets) under a sum/cost constraint is an **NP-complete** problem. The brute-force state space is "which bucket does each element go into," giving `k^n` possibilities.

## State Space

Each element can be placed into any of the `k` buckets, so there are `k^n` assignments to explore:

- `n` = length of the array
- `k` = number of partitions (buckets)

## Related Problems

See the following backtracking notes:

- Matchsticks to Square
- Partition to K Equal Sum Subsets
- Find Minimum Time to Finish All Jobs
