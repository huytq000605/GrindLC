class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        q = deque([(0, s1)])
        seen = set()
        n = len(s1)
        seen.add(s1)
        def swap_string(s, i, j):
            return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        while q:
            step, s = q.popleft()
            if s == s2:
                return step
            i = 0
            while s[i] == s2[i]:
                i += 1
            j = i + 1
            while j < n:
                if s[j] == s2[i] and s[j] != s2[j]:
                    new_s = swap_string(s, i, j)
                    if new_s not in seen:
                        seen.add(new_s)
                        q.append((step + 1, new_s))
                j += 1
        return -1