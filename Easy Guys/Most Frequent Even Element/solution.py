class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter()
        res_num, freq_num = -1, -1
        for num in nums:
            if num % 2 == 0:
                counter[num] += 1
                if counter[num] > freq_num or (freq_num == counter[num] and num < res_num):
                    freq_num = counter[num]
                    res_num = num
        return res_num
