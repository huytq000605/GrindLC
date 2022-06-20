class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = []
        before = [i for i in range(k)]
        after = []
        requests_handled = [0 for i in range(k)]
        
        for i in range(len(arrival)):
            start, time = arrival[i], load[i]
            server_id = i % k
            
            # Swap first and then return all freed node
            if server_id == 0:
                after, before = before, after

            while len(busy) and start >= busy[0][0]:
                if busy[0][1] >= server_id:
                    heappush(after, busy[0][1])
                else:
                    heappush(before, busy[0][1])
                heappop(busy)

                
            if len(after) == 0 and len(before) == 0:
                continue
            
            if len(after) > 0:
                server = heappop(after)
            else:
                server = heappop(before)
            
            heappush(busy, (start + time, server))
            requests_handled[server] += 1
            
        max_request = max(requests_handled)
        result = []
        for server, requests in enumerate(requests_handled):
            if requests == max_request:
                result.append(server)
        return result