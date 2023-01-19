class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        cur = 0
        result = 0
        for num in nums:
            cur = ((cur + num) % k + k) % k
            result += seen[cur]
            seen[cur] += 1
        return result
