class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []
        before = [i for i in range(k)]
        after = []
        used = [0 for _ in range(k)]

        for i, (t, l) in enumerate(zip(arrival, load)):
            server_id = i % k
            if server_id == 0:
                before, after = after, before
            
            while busy and busy[0][0] <= t:
                _, s = heappop(busy)
                if s >= server_id: heappush(after, s)
                else: heappush(before, s)
            
            if not before and not after: continue
            server = -1
            if after: server = heappop(after)
            else: server = heappop(before)
            used[server] += 1
            heappush(busy, (t + l, server))
        target = max(used)
        return [i for i, f in enumerate(used) if f == target]

                    
