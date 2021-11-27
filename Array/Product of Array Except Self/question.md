# 238. Product of Array Except Self<br> Medium

## Anduin Interview Question

There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

Example 1:

<pre>
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
</pre>

Example 2:

<pre>
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
</pre>

Constraints:

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- `The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.`

<details>

<summary> Related Topics </summary>

-   `Array`

</details>