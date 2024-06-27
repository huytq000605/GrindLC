class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        characters = set(target)
        @cache
        def dfs(mask):
            if mask == 0: return 0
            result = math.inf
            for sticker in stickers:
                used = dict()
                for c in sticker:
                    if c not in characters: continue
                    used[c] = used.get(c, 0) + 1
                
                next_mask = mask
                for i in range(len(target)):
                    if (next_mask >> i) & 1 and used.get(target[i], 0):
                        next_mask &= ~(1 << i)
                        used[target[i]] -= 1
                if next_mask != mask:
                    result = min(result, 1 + dfs(next_mask))
            return result

        result = dfs(2**len(target) - 1)
        return result if result != math.inf else -1
                
