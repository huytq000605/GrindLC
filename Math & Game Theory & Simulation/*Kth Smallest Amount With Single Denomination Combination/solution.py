class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        lcms_by_sz = defaultdict(list)
        for sz in range(1, len(coins)+1):
            for comb in itertools.combinations(coins, sz):
                lcms_by_sz[sz].append(math.lcm(*comb))

        start = min(coins)
        end = max(coins) * k
        while start < end:
            mid = start + (end - start) // 2
            
            valid = False
            kth = 0
                                
            for sz, lcms in lcms_by_sz.items():
                for lcm in lcms:
                    kth -= ((-1) ** sz) * (mid // lcm)

            if kth == k and valid:
                return mid
            elif kth < k:
                start = mid + 1
            else:
                end = mid
        return start
