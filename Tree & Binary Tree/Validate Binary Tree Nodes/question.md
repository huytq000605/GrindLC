# 1361. Validate Binary Tree Nodes<br> Medium

You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:

![](assets/1503_ex1.png)

<pre>
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
</pre>

Example 2:

![](assets/1503_ex2.png)

<pre>
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
</pre>

Example 3:

![](assets/1503_ex3.png)

<pre>
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
</pre>

Example 4:

![](assets/1503_ex4.png)

<pre>
Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false
</pre>

Constraints:

- `1 <= n <= 10^4`
- `leftChild.length == rightChild.length == n`
- `-1 <= leftChild[i], rightChild[i] <= n - 1`

<details>

<summary> Related Topics </summary>

-   `Tree`
-   `DFS`
-   `Union Find`

</details>