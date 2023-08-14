class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        used = defaultdict(int)
        pq = []
        free = []
        items.sort(key = lambda e: -e[0])
        for profit, category in items:
            if category not in used:
                used[category] += 1
                heappush(pq, (profit, category))
                if len(pq) > k:
                    p, c = heappop(pq)
                    used[c] -= 1
                    if used[c] == 0:
                        del used[c]
                    heappush(free, (-p, c))
            else:
                heappush(free, (-profit, category))

        while len(pq) < k:
            negative_p, c = heappop(free)
            heappush(pq, (-negative_p, c))
            used[c] += 1
            

        profits = 0
        for p, c in pq:
            profits += p

        while free:
            # hold
            hold = profits + len(used) ** 2
            # new
            new = profits - pq[0][0] + (-free[0][0]) + (len(used) - 1) ** 2
            if new > hold:
                cur_p, cur_c = heappop(pq)
                profits -= cur_p
                used[cur_c] -= 1
                if used[cur_c] == 0:
                    del used[cur_c]
                
                new_p, new_c = heappop(free)
                profits -= new_p
                used[new_c] += 1
                heappush(pq, (-new_p, new_c))
            else:
                break

        return profits + len(used) ** 2
