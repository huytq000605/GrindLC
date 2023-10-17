class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1 for _ in range(n)]
        
        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]
            if left != -1:
                if parent[i] == left: return False
                if parent[left] != -1: return False
                parent[left] = i
            if right != -1:
                if parent[i] == right: return False
                if parent[right] != -1: return False
                parent[right] = i

        root = -1
        for i in range(n):
            if parent[i] == -1:
                if root != -1: return False
                root = i
        
        seen = set([root])
        stack = [root]
        while stack:
            u = stack.pop()
            l, r = leftChild[u], rightChild[u]
            if l != -1:
                if l in seen: return False
                seen.add(l)
                stack.append(l)
            if r != -1:
                if r in seen: return False
                seen.add(r)
                stack.append(r)
        return len(seen) == n
