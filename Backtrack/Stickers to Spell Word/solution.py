class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        q = deque([(0, 0)])
        
        # Sort to do compare by two pointers
        stickers = list(map(sorted, stickers))
        target = sorted(target)
        seen = [0 for i in range(1<<n)]

        while q:
            mask, steps = q.popleft()
            bits = []
            for i in range(n):
                if (mask >> i) & 1: continue
                bits.append(i)
            
            for sticker in stickers:
                next_mask = mask
                i, j = 0, 0
                # Two pointers since to string is sorted
                while i < len(sticker) and j < len(bits):
                    while j < len(bits) and target[bits[j]] < sticker[i]:
                        j += 1
                    if j >= len(bits): continue
                    if sticker[i] == target[bits[j]]:
                        next_mask |= (1 << bits[j])
                        j += 1
                    i += 1

                if next_mask == mask or seen[next_mask]: continue
                if next_mask == (1<<n)-1: return steps + 1
                seen[next_mask] = 1
                q.append((next_mask, steps + 1))
        
        return -1