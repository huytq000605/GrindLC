class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        n = len(nums)
        pref = Counter()
        suf = Counter(nums)
        result = 0
        MOD = 10**9 + 7
        s = set(nums)
        for i, num in enumerate(nums):
            suf[num] -= 1
            left = i
            right = n-1-i
            # calculate how many options we can choose nums[i] with >= 2 times
            result += comb(left, 2) * comb(right, 2)
            result -= comb(left - pref[num], 2) * comb(right - suf[num], 2)
            # with nums[i] appears >= 2 times, we need to exclude the situations where
            # num appears 2 times, but num2 appears 3 times
            # num appears 2 times, num2 appears 2 times, and another number appears 1 time
            for num2 in s:
                if num2 == num: continue
                # num2 num2 num num num2
                result -= comb(pref[num2], 2) * suf[num] * suf[num2]
                # num2 num num num2 num2
                result -= pref[num2] * pref[num] * comb(suf[num2], 2)

                # num2 num2 num num other
                result -= comb(pref[num2], 2) * suf[num] * (right - suf[num] - suf[num2])
                # num2 num num num2 other
                result -= pref[num2] * pref[num] * suf[num2] * (right - suf[num] - suf[num2])
                # other num2 num num2 num
                result -= (left - pref[num2] - pref[num]) * pref[num2] * suf[num2] * suf[num]
                # other num num num2 num2
                result -= (left - pref[num2] - pref[num]) * pref[num] * comb(suf[num2], 2)
                
            pref[num] += 1
        return result % MOD
