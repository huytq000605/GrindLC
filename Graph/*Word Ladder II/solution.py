class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        WILDCARD = "."
        # Build graph for words by pattern
        def build_graph():
            words = set(wordList)
            graph = defaultdict(list)
            words.add(beginWord)
            for word in words:
                for i in range(len(word)):
                    pattern = word[:i] + WILDCARD + word[i+1:]
                    graph[pattern].append(word)
            return graph
        
        # Do BFS from beginWord to endWord, save every parents
        def bfs():
            q = deque([beginWord])
            parents = defaultdict(list)
            parents[beginWord] = []
            found = False
            while q and not found:
                nq = deque()
                current_level_parents = defaultdict(list)
                while q:
                    word = q.popleft()
                    for i in range(len(word)):
                        pattern = word[:i] + WILDCARD + word[i+1:]
                        for next_word in graph[pattern]:
                            if next_word == endWord:
                                found = True
                            if next_word not in parents:
                                if next_word not in current_level_parents:
                                    nq.append(next_word)
                                current_level_parents[next_word].append(word)               
                parents.update(current_level_parents)
                q = nq
            return parents

        # DFS from endWord to beginWord
        def dfs(word):
            nonlocal path, result
            if word == beginWord:
                result.append([*path])
            for parent in parents[word]:
                path.appendleft(parent)
                dfs(parent)
                path.popleft()

        graph = build_graph()
        parents = bfs()
        result = []
        path = deque([endWord])
        dfs(endWord)
        return result
