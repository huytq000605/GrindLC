class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        result = 0
        for num in nums:
            if k - num in seen:
                seen[k-num] -= 1
                result += 1
                if seen[k-num] == 0:
                    seen.pop(k - num)
            else:
                seen[num] += 1
        return result
            