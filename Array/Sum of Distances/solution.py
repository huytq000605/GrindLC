class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        idxs = defaultdict(list)
        cur = defaultdict(int)
        prefix = defaultdict(list)
        for i, num in enumerate(nums):
            idxs[num].append(i)
            cur[num] += i
            prefix[num].append(cur[num])
        
        n = len(nums)

        result = [0 for _ in range(n)]
        idx_in_idxs = defaultdict(int)
        for i in range(n):
            num = nums[i]
            idx = idx_in_idxs[num]
            m = len(idxs[num])
            if idx == 0: result[i] = prefix[num][-1] - idxs[num][idx] * m
            else: result[i] = (idxs[num][idx] * (idx - 1)) - prefix[num][idx-1] + (prefix[num][-1] - prefix[num][idx-1]) - (idxs[num][idx] * (m-1-idx))
            idx_in_idxs[num] += 1
        return result
