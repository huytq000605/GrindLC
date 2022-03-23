class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        max_score = 0
        max_mask = 0
        for mask in range(1 << 12):
            arrows = 0
            score = 0
            for i in range(12):
                 if (mask >> i) & 1 == 1:
                        arrows += aliceArrows[i] + 1
                        score += i
            if arrows > numArrows:
                continue
            if score > max_score:
                max_score = score
                max_mask = mask
        
        arr = [0 for i in range(12)]
        for i in range(12):
            if (max_mask >> i) & 1 == 1:
                arr[i] += aliceArrows[i] + 1
        arr[0] += numArrows - sum(arr)
        return arr