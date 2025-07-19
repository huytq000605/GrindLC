class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        trie = dict()
        for i, f in enumerate(folders):
            path = f.split('/')
            t = trie
            for j in range(1, len(path)):
                if path[j] not in t:
                    t[path[j]] = dict()
                t = t[path[j]]
            t['folder'] = i
        q = [trie]
        result = []
        while q:
            t = q.pop()
            if 'folder' in t:
                result.append(folders[t['folder']])
            else:
                for k in t:
                    q.append(t[k])
        return result
