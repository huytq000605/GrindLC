class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # We will maintain a sliding window, whenever AND goes below k
        # There's no point of adding more elements, because the value can only be lower
        # We try to move the start to the right and set the result during the process
        result = math.inf
        def cal_and(bits, length):
            result = 0
            for bit in range(30):
                if bits[bit] == length:
                    result += 1 << bit
            return result
        
        def add_num(bits, num):
            bit = 0
            while num:
                bits[bit] += num & 1
                num >>= 1
                bit += 1
        
        def remove_num(bits, num):
            bit = 0
            while num:
                bits[bit] -= num & 1
                num >>= 1
                bit += 1
        
        start = 0
        bits = [0 for _ in range(30)]
        for end, num in enumerate(nums):
            add_num(bits, num)
            cur_and = cal_and(bits, end - start + 1)
            result = min(result, abs(k - cur_and))
            while start <= end and cur_and < k:
                remove_num(bits, nums[start])
                start += 1
                if start <= end:
                    cur_and = cal_and(bits, end - start + 1)
                    result = min(result, abs(k - cur_and))
        return result
            
