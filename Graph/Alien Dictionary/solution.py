class Solution:
    def alienOrder(self, words: List[str]) -> str:
        degree = defaultdict(int)
        after = defaultdict(set)
        characters = set(words[0])
        for i in range(1, len(words)):
            prev = words[i-1]
            cur =  words[i]
            order = False
            for j in range(min(len(prev), len(cur))):
                if prev[j] == cur[j]: continue
                if cur[j] not in after[prev[j]]:
                    degree[cur[j]] += 1
                    after[prev[j]].add(cur[j])
                order = True
                break
            if not order and len(prev) > len(cur): return ""
            characters |= set(words[i])

        result = ""
        dq = deque()
        for c in characters:
            if c not in degree:
                result += c
                dq.append(c)

        while dq:
            c = dq.popleft()
            for next_c in after[c]:
                degree[next_c] -= 1
                if not degree[next_c]: 
                    result += next_c
                    dq.append(next_c)
        if len(result) != len(characters): return ""
        return result
