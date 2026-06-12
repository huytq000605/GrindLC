# Morris Traversal

**Idea:** Traverse a binary tree inorder or preorder in **O(1) space** — no stack, no recursion. To find the way back up after descending left, we temporarily rewire each node's inorder predecessor to point at the current node (a "threaded" link), then undo it once used.

> Morris Traversal **mutates the tree** while it runs. If write operations aren't allowed, you cannot use Morris Traversal.

## How it works

For each `current` node:
- **No left child:** visit it (logic differs slightly between inorder/preorder), then move right.
- **Has a left child:** find the `predecessor` — the rightmost node of the left subtree.
  - If the predecessor's `right` is `None`, set the thread (`predecessor.right = current`) and descend left.
  - If the predecessor's `right` already points back here, the left subtree is done — restore/advance and move right.

## Inorder

```python
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    current = root
    result = []
    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right != current and predecessor.right:
                predecessor = predecessor.right
            # traverse to current later
            if predecessor.right == None:
                predecessor.right = current
                current = current.left
            # predecessor is pointing to this node, so we need add this node to result and go to right
            else:
                result.append(current.val)
                current = current.right
    return result
```

## Preorder

```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    current = root
    result = []
    while current:
        result.append(current.val)
        if not current.left:
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right != current and predecessor.right:
                predecessor = predecessor.right
            # traverse to current.right later
            if predecessor.right == None:
                predecessor.right = current.right
                current = current.left
            # predecessor is pointing to this node, we've added it to result, so we go to the right
            else:
                current = current.right
    return result
```

## Complexity

- **Time:** O(n) — each edge is traversed at most twice (once to set the thread, once to follow it).
- **Space:** O(1) — only the threaded pointers are reused; no stack or recursion.
