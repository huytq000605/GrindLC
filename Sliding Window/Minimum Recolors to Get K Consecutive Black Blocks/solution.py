class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cur = 0
        longest = 0
        n = len(blocks)
        for i in range(n):
            if i >= k:
                if blocks[i-k] == "B":
                    cur -= 1
            if blocks[i] == "B":
                cur += 1
            longest = max(longest, cur)
        return max(0, k - longest)
