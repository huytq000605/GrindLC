class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        trees = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p == -1: continue
            trees[p].append((i, s[i]))
        result = 0
        # Store met trees by bitmask
        masks = defaultdict(int)
        masks[0] += 1
        def dfs(u, mask):
            nonlocal result, masks
            current = 0
            for v, c in trees[u]:
                c = ord(c) - ord('a')
                next_mask = mask ^ (1 << c)
                # Can have up to 1 set bit
                for i in range(26):
                    xor = next_mask ^ (1 << i)
                    if xor in masks:
                        result += masks[xor]
                        current += masks[xor]
                # 0 set bit
                if next_mask in masks: 
                    result += masks[next_mask]
                    current += masks[xor]
                masks[next_mask] += 1
                dfs(v, next_mask)
        dfs(0, 0)
        return result


                
