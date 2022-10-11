class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        state = []
        for num in nums:
            if not state or state[-1] < num:
                state.append(num)
            for i in range(len(state)):
                if state[i] >= num:
                    state[i] = num
                    break
            if len(state) == 3:
                return True
        return False
