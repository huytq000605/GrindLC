class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups_by_mod = [defaultdict(int) for _ in range(k)]
        for num in nums:
            groups_by_mod[num % k][num] += 1
        result = 1
        for mod, freqs in enumerate(groups_by_mod):
            if not freqs: continue
            prev = -math.inf
            prev_not_taken = 1 # empty subset
            prev_taken = 0
            for num in sorted(freqs.keys()):
                freq = freqs[num]
                possible_subsets = (2**freq) - 1 # minus 1 for empty subset
                if prev + k == num:
                    taken = prev_not_taken * possible_subsets
                    not_taken = prev_taken + prev_not_taken
                else:
                    taken = (prev_taken + prev_not_taken) * possible_subsets
                    not_taken = prev_taken + prev_not_taken
                prev_taken = taken
                prev_not_taken = not_taken
                prev = num
            result *= (prev_taken + prev_not_taken)
        return result - 1
