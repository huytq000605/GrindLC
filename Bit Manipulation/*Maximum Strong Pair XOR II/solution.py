class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0
        for bit in range(20, -1, -1):
            target = (max_xor >> bit) | 1
            prefixes_min = dict() # store minimum num has prefix
            prefixes_max = dict() # store maximum num has prefix
            for num in nums:
                prefix = num >> bit
                if prefix not in prefixes_min:
                    prefixes_min[prefix] = prefixes_max[prefix] = num
                prefixes_min[prefix] = min(prefixes_min[prefix], num)
                prefixes_max[prefix] = max(prefixes_max[prefix], num)
            # |x - y| <= min(x, y)
            # assume x >= y
            # x - y <= y
            # x <= 2y
            for a in prefixes_min.keys():
                b = target ^ a
                if b in prefixes_max and a >= b and\
                    prefixes_min[a] <= prefixes_max[b] * 2:
                        max_xor |= (1 << bit)
                        break
        return max_xor
