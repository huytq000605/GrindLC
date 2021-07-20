# 1722. Minimize Hamming Distance After Swap Operations<br> Medium

You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.

The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.

Example 1:

<pre>
Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
Output: 1
Explanation: source can be transformed the following way:
- Swap indices 0 and 1: source = [2,1,3,4]
- Swap indices 2 and 3: source = [2,1,4,3]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
</pre>

Example 2:

<pre>
Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
Output: 2
Explanation: There are no allowed swaps.
The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
</pre>

Constraints:

- `n == source.length == target.length`
- `1 <= n <= 10^5`
- `1 <= source[i], target[i] <= 10^5`
- `0 <= allowedSwaps.length <= 10^5`
- `allowedSwaps[i].length == 2`
- `0 <= ai, bi <= n - 1`
- `ai != bi`


<details>

<summary> Related Topics </summary>

-   `Union Find`
-   `Depth-first Search`

</details>

<details>

<summary> Hint 1 </summary>
The source array can be imagined as a graph where each index is a node and each allowedSwaps[i] is an edge.
</details>
<details>

<summary> Hint 2 </summary>
Nodes within the same component can be freely swapped with each other.
</details>

<details>
<summary> Hint 3 </summary>
For each component, find the number of common elements. The elements that are not in common will contribute to the total Hamming distance.
</details>