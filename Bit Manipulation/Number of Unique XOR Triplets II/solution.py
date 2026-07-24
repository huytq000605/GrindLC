class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pairs = [0 for _ in range(1 << 10 + 1)]
        for num1 in nums:
            for num2 in nums:
                pairs[num1^num2] = 1
        xors = [0 for _ in range(1 << 10 + 1)]
        for num in nums:
            for pair, ok in enumerate(pairs):
                if not ok: continue
                xors[num^pair] = 1
        return sum(xors)
