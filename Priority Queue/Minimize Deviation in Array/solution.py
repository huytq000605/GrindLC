class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        result = math.inf
        min_num = math.inf
        pq = []
        # to minize the diff between max & min
        # need to decrease max or increase min
        # even number never increase
        # because the even number can turn back to odd number again
        # we make the whole array even, then decrease the max
        for num in nums:
            if num % 2:
                num *= 2
            min_num = min(min_num, num)
            heappush(pq, -num)
        
        while -pq[0] % 2 == 0:
            max_num = -heappop(pq)
            result = min(result, max_num - min_num)
            min_num = min(min_num, max_num // 2)
            heappush(pq, -(max_num // 2))
            
        return min(result, -pq[0] - min_num)
