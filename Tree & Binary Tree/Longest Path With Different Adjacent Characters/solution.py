class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(set)
        for node, parent in enumerate(parent):
            if node == 0:
                continue
            tree[parent].add(node)
        ans = 0
        def dfs(node):
            nonlocal ans
            arr = []
            result = 1
            for subtree in tree[node]:
                path = dfs(subtree)
                ans = max(ans, path)
                if s[node] != s[subtree]:
                    heappush(arr, path)
                    result = max(result, path + 1)
                    if len(arr) > 2:
                        heappop(arr)
            if len(arr) == 2:
                ans = max(ans, sum(arr) + 1)
            return result
        single_tree = dfs(0)
        return max(single_tree, ans)