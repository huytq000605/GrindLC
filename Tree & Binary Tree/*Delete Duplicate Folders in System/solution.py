class Solution:    
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        IDX = 'IDX'
        VAL = 'VAL'
        paths.sort()
        tree = dict()
        tree[IDX] = -1
        for i, path in enumerate(paths):
            t = tree
            for f in path:
                if f not in t:
                    t[f] = dict()
                t = t[f]
            t[IDX] = i
        seen = dict()
        removed = [False for _ in range(len(paths))]
        def dfs(t):
            stree = ""
            for k in t:
                if k == IDX or k == VAL: continue
                s = dfs(t[k])
                stree += f"({k}{s})"
            # having the same non empty subtree => remove
            if stree and stree in seen:
                removed[seen[stree][IDX]] = True
                removed[t[IDX]] = True
                # marking all the subtrees to be removed as well
                for k in seen[stree]:
                    if k == IDX or k == VAL: continue
                    removed[seen[stree][k][IDX]] = True
                for k in t:
                    if k == IDX or k == VAL: continue
                    removed[t[k][IDX]] = True
            elif t != tree:
                seen[stree] = t
            return stree
        dfs(tree)
        result = []
        for i in range(len(paths)):
            if removed[i]: continue
            result.append(paths[i])
        return result
