class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        freq_freq = defaultdict(int)
        result = 0
        for i, num in enumerate(nums):
            if freq[num] != 0:
                freq_freq[freq[num]] -= 1
                
            if freq_freq[freq[num]] == 0:
                freq_freq.pop(freq[num])
            freq[num] += 1
            freq_freq[freq[num]] += 1
            if len(freq_freq) <= 2:
                if len(freq_freq) == 1:
                    # only one number
                    if len(freq) == 1:
                        result = i + 1
                    # all numbers appear only 1 time
                    if list(freq_freq.keys())[0] == 1:
                        result = i + 1
                else:
                    i1, i2 = sorted(list(freq_freq.items()))
                    k1, v1 = i1
                    k2, v2 = i2
                    if (k1 == 1 and v1 == 1) or (k1 - k2 == 1 and v1 == 1) or (k2 - k1 == 1 and 2 == 1):
                        result = i + 1
            
        return result
