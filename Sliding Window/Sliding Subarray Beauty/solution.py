class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        counter = Counter()
        result = []
        for i, num in enumerate(nums):
            if i >= k:
                counter[nums[i-k]] -= 1
            counter[num] += 1
            if i >= k-1:
                m = x
                for num in range(-50, 0):
                    m -= counter[num]
                    if m <= 0: 
                        result.append(num)
                        break
                if m > 0:
                    result.append(0)
        return result
