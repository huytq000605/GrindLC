class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        
        ln = defaultdict(list)
        for i, num in enumerate(nums):
            ln[num].append(i)
        n = len(nums)
        result = n-1
        for idxs in ln.values():
            idxs = [*idxs, n + idxs[0]]
            steps = 0
            for i in range(1, len(idxs)):
                steps = max(steps, (idxs[i] - idxs[i-1]) // 2)
            result = min(result, steps)

        return result
