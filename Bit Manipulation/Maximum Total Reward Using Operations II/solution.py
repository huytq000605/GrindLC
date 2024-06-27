class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        # first bit denote s = 0
        s = 1
        for r in rewardValues:
            # can only apply r for values < r
            mask = (1<<r) - 1
            # apply r for all values < r and preserve all the previous s
            s |= (s & mask) << r
        # return the biggest number which is MSB
        return s.bit_length() - 1
