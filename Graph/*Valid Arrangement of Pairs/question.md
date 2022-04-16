# 2097. Valid Arrangement of Pairs<br> Hard

You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.

Return any valid arrangement of pairs.

Note: The inputs will be generated such that there exists a valid arrangement of pairs.

Example 1:

<pre>
Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
Output: [[11,9],[9,4],[4,5],[5,1]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 9 == 9 = start1 
end1 = 4 == 4 = start2
end2 = 5 == 5 = start3
</pre>

Example 2:

<pre>
Input: pairs = [[1,3],[3,2],[2,1]]
Output: [[1,3],[3,2],[2,1]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 3 == 3 = start1
end1 = 2 == 2 = start2
The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.
</pre>

Constraints:

- `1 <= pairs.length <= 10^5`
- `pairs[i].length == 2`
- `0 <= starti, endi <= 10^9`
- `starti != endi`
- `No two pairs are exactly the same.`
- `There exists a valid arrangement of pairs`

<details>

<summary> Related Topics </summary>

-   `Graph`
-   `Euler Path`

</details>