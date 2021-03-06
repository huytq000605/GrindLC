# 968. Binary Tree Cameras<br> Hard

You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:

![](assets/bst_cameras_01.png)

<pre>
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
</pre>

Example 2:

![](assets/bst_cameras_02.png)

<pre>
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
</pre>

Constraints:

-   `Tree`
-   `DFS`
-   `Greedy`

<details>