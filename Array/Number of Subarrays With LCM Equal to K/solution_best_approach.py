class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        result = 0
        m = defaultdict(int)
        for num in nums:
            m1 = defaultdict(int)
            if k % num == 0:
                m1[num] += 1
                for lcm, freq in m.items():
                    m1[math.lcm(lcm, num)] += freq
                result += m1[k]
            m = m1
        return result
