class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        prefix = [0 for i in range(n)]
        result = defaultdict(set)
        ans = 0
        for i, num in enumerate(nums):
            if i > 0:
                prefix[i] = prefix[i-1]
            if num % p == 0:
                prefix[i] += 1
            
        for length in range(1, n+1):
            for start in range(0, n - length + 1):
                end = start + length - 1
                prev = 0
                if start > 0:
                    prev = prefix[start-1]
                
                if prefix[end] - prev > k:
                    continue
								# Use this in another programming language
                # result[length].add("a".join(map(str, nums[start:end + 1])))
                result[length].add(tuple(nums[:start:end+1]))
            ans += len(result[length])
        return ans