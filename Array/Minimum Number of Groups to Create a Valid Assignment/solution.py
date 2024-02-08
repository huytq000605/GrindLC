class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        counter = Counter(nums)
        freqs = counter.values()

        def count(freqs, k):
            result = 0
            for freq in freqs:
                groups = freq // (k+1)
                remaining = freq % (k+1)
                # every group with k + 1 nums can give to last group
                if remaining > 0:
                    if groups + remaining < k:
                        return 0
                    groups += 1
                result += groups
            return result

        # each group can have up to min(freqs) nums
        # time complexity: O(min(freqs) * len(freqs)) <= O(sum(freqs)) <= O(n)
        for each in reversed(range(1, min(freqs) + 1)):
            groups = count(freqs, each)
            if groups:
                return groups
        return len(nums)

            
