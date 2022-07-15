# Morris Traversal

## If we want to traverse a tree by inorder or preorder without a stack or recursion, only O(1) space, we need to use Morris Traversal
## Morris Traversal mutates the tree on the way, so if we cannot do write operation, then we cannot do Morris Traversal

## Inorder
``` python
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
``` python
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
