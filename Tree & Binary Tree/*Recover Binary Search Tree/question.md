# 99. Recover Binary Search Tree<br> Medium

## You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:

![](assets/recover1.jpg)

<pre>
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
</pre>

Example 2:

![](assets/recover2.jpg)

<pre>
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
</pre>

Constraints:

- `The number of nodes in the tree is in the range [2, 1000].`
- `-2^31 <= Node.val <= 2^31 - 1`

<details>

<summary> Related Topics </summary>

-   `Tree`
-   `Depth-first Search`

</details>
