class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        graph = [[] for _ in range(n)]
        same = defaultdict(list)
        for i, num in enumerate(arr):
            same[num].append(i)
        seen = [0 for _ in range(n)]
        seen[0] = 1
        q = deque([(0, 0)])
        while q:
            i, s = q.popleft()
            if i == n-1: return s
            if i - 1 >= 0 and not seen[i-1]:
                seen[i-1] = 1
                q.append((i-1, s+1))
            if i + 1 < n and not seen[i+1]:
                seen[i+1] = 1
                q.append((i+1, s+1))
            for ni in same[arr[i]]:
                if not seen[ni]:
                    if ni == n-1:
                        return s+1
                    seen[ni] = 1
                    q.append((ni, s+1))
            same[arr[i]] = []
        return -1
