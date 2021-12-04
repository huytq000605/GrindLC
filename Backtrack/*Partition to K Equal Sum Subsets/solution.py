class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse = True)
        states = [0 for i in range(k)]
        
        def dfs(numIdx):
            if numIdx >= len(nums):
                return True
            seen = set()
            for stateIdx, state in enumerate(states):
                if state in seen or state + nums[numIdx] > target:
                    continue
                seen.add(state)
                states[stateIdx] += nums[numIdx]
                if(dfs(numIdx + 1)): return True
                states[stateIdx] -= nums[numIdx]
            return False
        return dfs(0)