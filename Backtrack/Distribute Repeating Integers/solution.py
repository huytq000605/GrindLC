class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        counter = Counter(nums)
        freq = sorted(counter.values(), reverse = True)
        quantity.sort(reverse = True)
        
        def dfs(idx):
            if idx >= len(quantity):
                return True
            seen = set()
            for i, f in enumerate(freq):
                if f in seen or f < quantity[idx]:
                    continue
                freq[i] = f - quantity[idx]
                if dfs(idx + 1):
                    return True
                freq[i] = f
            return False
        
        return dfs(0)